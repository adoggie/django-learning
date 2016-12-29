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
echo / touch / source / export 
getconf LONG_BIT
cat /etc/release-***
hostname / hostnamectl / uname -a / ulimit /sysctl -a 
useradd / passwd 
chown / chgrp / chmod




1. top /htop / free -m / df / du / ps -e -opid,pcpu,comm|sort -n +1
2. vi/vim/nano/less/emacs
   ".vimrc "
3. wget/curl 
4. setsid / nohup / > dev/null 2>&1 / jobs / fg/bg 
5. tmux / screen 
6. nc -l xxxx / nmap / netstat -an / lsof -i:8080 
7. strings / tail -nf / head / watch / wc / cat 
8. awk / sed / tr 
9. pkill / pgrep / kill / ps 
10.grep / find / xargs -l {} /
11. ssh / scp / sshfs / samba / nfs 
12. tar / bzip / xy / zip / dd 
13. http server :  httpd / nginx / mongoose / python -m SimpleHTTPServer 8080 
14. iptables / selinux
15. rsync -rvat  src dest 
16. cron / ntpd
   (crontab -e)    /etc/crontab
   service crond start
17. svn / svnserve / 
18. vnc-server 
   yum install tigervnc-server 
   vncserver --geometry 600x450 
   vncviewer xxxxx:1 
19. webssh : shellinaboxd 

20. seq -s \  10 20 |  
    echo "xxx" | md5sum -b 
    echo "abc" | base64 | base64 -d 
      
   
   
   
"sshd  配置无需密码登录 "
      vim /etc/ssh/ssh_config
         StrictHostKeyChecking no
      service sshd restart
      
      生成公私钥： ssh-keygen -t rsa  -> ~/.ssh/id_rsa.pub | id_rsa
      在登录目标主机文件 ~/.ssh/authorized_keys 添加本机的公钥内容( id_rsa.pub) 
      
System Configurations:
---------------
/etc/resolv.conf 
/etc/hosts
/etc/hostname
/etc/release-***
/etc/network-scripts/ifcfg-eth0 
/dev/shm/


Pythons
--------
pip / easy_install / requiments.txt 
virtualenv 





