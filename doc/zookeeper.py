

默认端口 ：  2181  

zkServer  start/start-foreground / stop 
zkCli  
zkCli.sh -server 127.0.0.1:2181
  
>connect localhost:port

>telnet  localhost:port 
>state


python 支持 
----------------
由于python客户端依赖c的客户端所以要先安装c版本的客户端

cd zookeeper-3.4.5/src/c  
./configure  
make   
make install

pip install zkpython 

https://github.com/stfp/zkpython

  
图形管理接口 :  
  pycharm IDE中安装插件
  zookeeper , mongodb
  

  编程指南：
    http://zookeeper.apache.org/doc/r3.5.0-alpha/zookeeperProgrammers.html
    
  Ephemeral Node - 临时节点  
  EPHEMERAL_SEQUENTIAL-临时顺序编号目录节点 
  PERSISTENT-持久化目录节点 
  PERSISTENT_SEQUENTIAL-持久化顺序编号目录节点
  
  Watches EVents:  Created,Deleted,Changed,Child
  ACLs - 访问控制列表(Permissions) : CREATE,READ,WRITE,DELETE,ADMIN
    
 ? - 考虑Nginx反向代理服务器集群地址从zookeeper获取
  
  
  
