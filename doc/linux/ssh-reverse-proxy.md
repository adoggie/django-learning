

# Ssh 建立反向代理服务

开发场景中，需要公网主机的端口映射到内网开发主机端口,

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

 
