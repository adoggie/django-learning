Postgresql
-----------
1. installation
   yum  install postgresql-server postgresql-devel
   
2. initialization
   service postgresql initdb     ( /var/lib/pgsql/data) 
    su - postgres -c "initdb -D /opt/pgsql" 
   
3. running & tunning 
   service postgresql start|stop|restart 
   "pg_ctl -D /var/lib/pgsql start "
   
   
   "pg_hba.conf" :  访问控制，主机、用户、认证方式
   "postgresql.conf" :  数据库实例运行参数，默认采用 unix socket 
   
4. create & config 
   su - postgres 
   pql 
   create database testdb;
   alter user postgres with password "xxxx" 
   
software installation
--------------
1. 不应该使用root安装应用软件，创建独立的用户和用户组，并设置对应的文件控制权限
2. chroot
3. docker

   
Tools
----------

yum: 
   yumdownloader 
   source files: /etc/yum.repos.d/xxxx 
   yum install|search|remove|update
   yum install epel-release 
   

command types:  1.builtin ; 2. external

man 1,2,3,4,5
echo / touch / source / export / whereis / uptime /last 
getconf LONG_BIT
time / date /times
cat /etc/release-***
hostname / hostnamectl / uname -a / ulimit /sysctl -a 
useradd / passwd 
chown / chgrp / chmod




1. top /htop / free -m / df / du / ps -e -opid,pcpu,comm|sort -n +1
   free -m 
   du --max-depth  --exclude 
2. vi/vim/nano/less/emacs
   ".vimrc "
3. wget/curl 
   curl -X POST -d '{"auth”: {"passwordCredentials":{"username": "admin", "password": "605ab45d701f4256"}}}' -H "Content-type: application/json" http://172.16.10.249:5000/v2.0/tokens | python -mjson.tool
http://docs.openstack.org/developer/python-swiftclient/client-api.html#examples
   
4. setsid / nohup / > dev/null 2>&1 / jobs / fg/bg 
5. tmux / screen 
6. nc -l xxxx / nmap / netstat -an / lsof -i:8080 
7. file / strings / tail -nf / head / watch / wc / cat 
8. awk / sed / tr 
9. pkill / pgrep / kill / ps / killall
10.grep / find / xargs
   grep -v 排除过滤范围  
   xargs 管道输出作为下级命令的输入参数 
        xargs -I {}    {} 作为占位符使用，功能强大
   find ./ | grep .cpp | xargs -I {}  mv {} {}.back    -- 将当前目录下.cpp文件加上.back后缀 

   
11. ssh / scp / sshfs / samba / nfs / rsync -rvat  src dest 
   ssh me@host "command;"
12. tar / bzip / xy / zip / dd 
13. http server :  httpd / nginx / mongoose / python -m SimpleHTTPServer 8080 
14. iptables / selinux
15. pwgen 10 1 
16. cron / ntpd
   (crontab -e)    /etc/crontab
   service crond start
17. svn / svnserve / 
18. vnc-server 
   yum install tigervnc-server 
   vncserver --geometry 600x450 
   vncviewer xxxxx:1 
19. webssh : shellinaboxd 
20.ifconfig / route / ping / traceroute / nslookup
   ifconfig eth0 
   ifconfig eth0 192.168.0.22 netmask 255.255.255.0 
   
20. seq -s \  10 20 |  
    echo "xxx" | md5sum -b 
    echo "abc" | base64 | base64 -d 

21. iotop / nload /nmon / lshw 

   
   
   
"sshd  配置无需密码登录 "
      vim /etc/ssh/ssh_config
         StrictHostKeyChecking no
      service sshd restart
      
      生成公私钥： ssh-keygen -t rsa  -> ~/.ssh/id_rsa.pub | id_rsa
      在登录目标主机文件 ~/.ssh/authorized_keys 添加本机的公钥内容( id_rsa.pub) 
      
System Configurations:
---------------
~/.bash_profile  
/etc/profile 
/etc/ld.so.conf    /etc/ld.so.conf.d
    ldconfig


/etc/resolv.conf 
/etc/hosts
/etc/hostname
/etc/release-***
/etc/network-scripts/ifcfg-eth0 
/dev/shm/
/proc/cupinfo
/proc/meminfo



Pythons
--------
pip / easy_install / requiments.txt 
virtualenv 





