

# Ssh 建立反向代理服务

开发场景中，需要公网主机的端口映射到内网开发主机端口,

#### 简单方法：
> linux 安装nginx启动tcp/http的 转向 pass_xxx , mac/windows 安装 termius或 xshell 。 

1.remote 模式（反向）  app --> linux --> mac(http) 

外网用户请求通通ng+ssh转向到本地开发主机 

2. local 模式（正向） mac -> linux  

本地主机利用ssh访问linux主机才能访问的服务，等同ssh开了个后门允许访问安全策略的内网服务主机


> Centos具有公网Ip，在Centos上开启正向代理，在Mac上开启反向代理

## Mac :  
<pre>
    ssh -CNfR 35002:127.0.0.1:25002 root@yangui
    将远端的25002 转到本机的25002 端口
</pre>

## Centos: 
<pre>
ssh -fCNL *:25002:localhost:35002 localhost  
    将对外的25002端口转向centos本机的35002端口
</pre>

## 命令
<pre>
netstat -ntpl 
fuser -v 25002/tcp
ssh-copy-id root@host  免密码登录
</pre>

 
