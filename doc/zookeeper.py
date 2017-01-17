

默认端口 ：  2181  

zkServer  start/start-foreground / stop 
zkCli  
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
