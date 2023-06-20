
```
关闭selinux
SELINUX=disabled 


关闭 防火墙 ，打开 iptables
systemctl disable firewalld.service 


安装iptables
yum install iptables-services
systemctl enable iptables 
systemctl start iptables 


vim /etc/sysctl.conf
│net.ipv4.ip_forward = 1
sysctl -p 
sysctl -w net.ipv4.ip_forward = 1
```

```

apt update
yum install -y openssl lzo pam openssl-devel lzo-devel pam-devel easy-rsa openvpn


cp -rf /usr/share/easy-rsa/3.0.8 /etc/openvpn/server/easy-rsa
cd /etc/openvpn/server/easy-rsa
./easyrsa init-pki
./easyrsa build-ca nopass
./easyrsa gen-dh
./easyrsa build-server-full server nopass

openvpn --genkey --secret ta.key


 生成Diffle Human参数，它能保证密钥在网络中安全传输

创建使用的目录

mkdir -p /var/log/openvpn/
mkdir -p /etc/openvpn/server/user
chown openvpn:openvpn /var/log/openvpn


cat << EOF > /etc/openvpn/server.conf
port 1194
proto tcp-server
dev tun
user openvpn
group openvpn
ca /etc/openvpn/server/easy-rsa/pki/ca.crt
cert /etc/openvpn/server/easy-rsa/pki/issued/server.crt
key /etc/openvpn/server/easy-rsa/pki/private/server.key
dh /etc/openvpn/server/easy-rsa/pki/dh.pem
tls-auth /etc/openvpn/server/easy-rsa/ta.key 0
auth-user-pass-verify /etc/openvpn/server/user/checkpsw.sh via-env
script-security 3
verify-client-cert
username-as-common-name
;client-to-client
## Allow multiple clients with the same common name to concurrently connect.
duplicate-cn
server 10.8.0.0 255.255.255.0
#route 10.8.1.0 255.255.255.0
#route 10.8.2.0 255.255.255.0
push "dhcp-option DNS 114.114.114.114"
push "dhcp-option DNS 8.8.8.8"
push "route 10.8.0.0 255.255.255.0"
push "route 172.16.20.0 255.255.255.0"
push "route 172.16.30.0 255.255.255.0"
#route 172.16.20.0 255.255.255.0
#route 172.16.30.0 255.255.255.0
#compress lzo
#ncp-ciphers "AES-256-GCM:AES-128-GCM"
keepalive 10 120
persist-key
persist-tun
verb 3
log /var/log/openvpn/server.log
log-append /var/log/openvpn/server.log
status /var/log/openvpn/status.log
;cipher AES-256-GCM
#client-config-dir /etc/openvpn/ccd

EOF



创建用户密码文件
格式是用户 密码以空格分割即可
cat << EOF > /etc/openvpn/server/user/psw-file
sam sam123
hr hr123
EOF

chmod 600 /etc/openvpn/server/user/psw-file
chown openvpn:openvpn /etc/openvpn/server/user/psw-file
chmod +x /etc/openvpn/server/user/psw-file

vim /etc/openvpn/server/user/checkpsw.sh 

#!/bin/sh
###########################################################
# checkpsw.sh (C) 2004 Mathias Sundman <mathias@openvpn.se>
#
# This script will authenticate OpenVPN users against
# a plain text file. The passfile should simply contain
# one row per user with the username first followed by
# one or more space(s) or tab(s) and then the password.
PASSFILE="/etc/openvpn/server/user/psw-file"
LOG_FILE="/var/log/openvpn/password.log"
TIME_STAMP=`date "+%Y-%m-%d %T"`
###########################################################
if [ ! -r "${PASSFILE}" ]; then
  echo "${TIME_STAMP}: Could not open password file \"${PASSFILE}\" for reading." >>  ${LOG_FILE}
  exit 1
fi
CORRECT_PASSWORD=`awk '!/^;/&&!/^#/&&$1=="'${username}'"{print $2;exit}' ${PASSFILE}`
if [ "${CORRECT_PASSWORD}" = "" ]; then
  echo "${TIME_STAMP}: User does not exist: username=\"${username}\", password=
\"${password}\"." >> ${LOG_FILE}
  exit 1
fi
if [ "${password}" = "${CORRECT_PASSWORD}" ]; then
  echo "${TIME_STAMP}: Successful authentication: username=\"${username}\"." >> ${LOG_FILE}
  exit 0
fi
echo "${TIME_STAMP}: Incorrect password: username=\"${username}\", password=
\"${password}\"." >> ${LOG_FILE}
exit 1

chown openvpn:openvpn /etc/openvpn/server/user/checkpsw.sh 
chmod +x /etc/openvpn/server/user/checkpsw.sh 

systemctl enable openvpn@server
systemctl restart openvpn@server
systemctl status openvpn@server

echo 1 > /proc/sys/net/ipv4/ip_forward

/usr/sbin/openvpn --daemon ovpn-server --status /run/openvpn/server.status 10 --cd /etc/openvpn --script-security 2 --config /etc/openvpn/server.conf --writepid /run/openvpn/server.pid





vim /etc/openvpn/server/make_user.sh

name=$1
crtdir=/etc/openvpn/server/crt
usercert=$crtdir/$name
mkdir -p $usercert

cd /etc/openvpn/server/easy-rsa/
/etc/openvpn/server/easy-rsa/easyrsa build-client-full $name nopass 

cp /etc/openvpn/server/easy-rsa/pki/issued/$name.crt $usercert
cp /etc/openvpn/server/easy-rsa/pki/private/$name.key $usercert
cp /etc/openvpn/server/easy-rsa/pki/ca.crt $usercert
cp /etc/openvpn/server/easy-rsa/ta.key $usercert


cat <<EOF > $usercert/base.conf
client
proto tcp-client
dev tun
auth-user-pass
remote 58.34.214.162 7777
#tls-auth ta.key 1
remote-cert-tls server
auth-nocache
persist-tun
persist-key
;compress lzo
verb 4
mute 10
key-direction 1
EOF
bash /etc/openvpn/server/make_config.sh $name

bash /etc/openvpn/server/make_user.sh sam
bash /etc/openvpn/server/make_config.sh sam




vim /etc/openvpn/server/make_config.sh
#!/bin/bash
 
# First argument: Client identifier

 
BASE_CONFIG=/etc/openvpn/server/crt/${1}/base.conf
 
cat ${BASE_CONFIG} \
    <(echo -e '<ca>') \
    /etc/openvpn/server/easy-rsa/pki/ca.crt \
    <(echo -e '</ca>\n<cert>') \
    /etc/openvpn/server/crt/${1}/${1}.crt \
    <(echo -e '</cert>\n<key>') \
   /etc/openvpn/server/crt/${1}/${1}.key \
    <(echo -e '</key>\n<tls-auth>') \
    /etc/openvpn/server/easy-rsa/ta.key \
    <(echo -e '</tls-auth>') \
    > /etc/openvpn/server/crt/${1}.ovpn

chmod +x /etc/openvpn/server/make_config.sh


vim ecosystem.config.js

module.exports={
apps:[
{name:'vpn',script:'ssh -CNR :7777:127.0.0.1:1194 -p 19015 elgt@bzz.wallizard.com -o TCPKeepAlive=yes -o ServerAliveInterval=30 -o ServerAliveCountMax=99999',autorestart:true,watch:false},
]
}

pm2 start 
pm2 save 
pm2 startup


证书吊销
1. 进入 OpenVPN 安装目录的 easy-rsa 子目录。例如我的为 /openvpn-2.0.5/easy-rsa/:
cd /etc/openvpn/easy-rsa

2. 执行 vars 命令
. vars

3. 使用 revoke-full 命令，吊销客户端证书。命令格式为：
revoke-full 
是VPN 客户端证书的用户名称。例如：
./revoke-full client1

这条命令执行完成之后， 会在 keys 目录下面， 生成一个 crl.pem 文件，这个文件中包含了吊销证书的名单。
成功注销某个证书之后，可以打开　keys/index.txt 文件，可以看到被注销的证书前面，已标记为R．

4. 确保服务端配置文件打开了 crl-verify 选项
在服务端的配置文件 server.conf 中，加入这样一行：
crl-verify crl.pem

如果 server.conf 文件和 crl.pem 没有在同一目录下面，则 crl.pem 应该写绝对路径，例如:

crl-verify /etc/openvpn/easy-rsa/keys/crl.pem

5. 重启 OpenVPN 服务。




netstat -nr | head -n 20
iptables -t nat -A POSTROUTING -s 10.18.0.0/24 -o ens192 -j MASQUERADE
iptables -L -n -t nat
iptables -t nat -D PREROUTING 2



公司人员 
10.8.0.0/24
管理员
10.8.0.0/24
实习生/外部人员
10.8.2.0/24

外部人员控制
iptables -t nat -A POSTROUTING -s 10.18.2.0/24 -o ens192 -j MASQUERADE
iptables -I FORWARD -s 10.18.2.0/24 -d 172.16.30.0/24 -j DROP

ccd/hr
ifconfig-push 10.8.2.5 10.8.2.6

[  1,  2] [  5,  6] [  9, 10] [ 13, 14] [ 17, 18]
[ 21, 22] [ 25, 26] [ 29, 30] [ 33, 34] [ 37, 38]
[ 41, 42] [ 45, 46] [ 49, 50] [ 53, 54] [ 57, 58]
[ 61, 62] [ 65, 66] [ 69, 70] [ 73, 74] [ 77, 78]
[ 81, 82] [ 85, 86] [ 89, 90] [ 93, 94] [ 97, 98]
[101,102] [105,106] [109,110] [113,114] [117,118]
[121,122] [125,126] [129,130] [133,134] [137,138]
[141,142] [145,146] [149,150] [153,154] [157,158]
[161,162] [165,166] [169,170] [173,174] [177,178]
[181,182] [185,186] [189,190] [193,194] [197,198]
[201,202] [205,206] [209,210] [213,214] [217,218]
[221,222] [225,226] [229,230] [233,234] [237,238]
[241,242] [245,246] [249,250] [253,254]

>>> [ x.split(',')[0] for x in [p.strip().replace(' ','').replace('[','') for p in s.split(']')] ]
['1', '5', '9', '13', '17', '21', '25', '29', '33', '37', '41', '45', '49', '53', '57', '61', '65', '69', '73', '77', '81', '85', '89', '93', '97', '101', '105', '109', '113', '117', '121', '125', '129', '133', '137', '141', '145', '149', '153', '157', '161
', '165', '169', '173', '177', '181', '185', '189', '193', '197', '201', '205', '209', '213', '217', '221', '225', '229', '233', '237', '241', '245', '249', '253', '']


vim /etc/openvpn/server/make_ccd.sh

bash make_ccd.sh 10.8.2 81

subnet=$1
start=$2
if [ -z "$1" ]
  then
    subnet="10.8.2"
fi

if [ -z "$2" ]
  then
    start=5
fi
end=$(($start + 1))
echo ifconfig-push $subnet.$start $subnet.$end



mkpasswd 
mkpasswd -l 12 -d 3 -C 3 -s 0


```
