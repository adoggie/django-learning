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
   
