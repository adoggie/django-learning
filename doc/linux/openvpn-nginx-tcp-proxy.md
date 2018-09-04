

#Openvpn实现 Tcp反向穿透 

>通过架设公网主机vpn建立隧道网络，实现公网两端主机通信连接


主机一览
--------

>公网服务器 （S) ：  101.231.207.51
<pre>
端口： 
  25003  openvpn 通信端口
  25002  nginx 代理服务端口
  25001  ssh管理
</pre>

>mac 主机: (C1)
<pre>
25002 接收
</pre>


>windows测试主机 (C2) 



服务器 S 配置： 
-------------

安装 nginx 1.9+ 

>vim /etc/nginx/nginx.conf

<pre>
stream {
        upstream stream_backend{
                server 10.8.0.6:25002;
        }
        server {
                listen 25002;
                proxy_pass stream_backend;
        }
}
</pre>

nginx -s reload 


vim /home/vpn/server.conf 
修改 port 为 25003  ( opevpn的服务端口) 

启动openvpn
openvpn --config /home/vpn/server.conf 


Mac主机 (C1) 
-------
>安装 tunnelblick
>修改 client.conf
  
 <pre>
  remote 101.231.207.51 25003
  ca ca.crt
  cert zhangbin.crt
  key zhangbin.key
 </pre>
 
>启动 tunnelblick - client.conf 

登录成功，服务器S分配vpn地址  10.8.0.6 

启动侦听测试: 
>nc -l 25002  # 必须与服务器S的nginx.conf配置的反向地址一样 


Windows主机(C2)
------
>启动测试  telnet 101.231.207.51 25002 


