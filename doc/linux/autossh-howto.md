
## autossh 配置主机穿透

> 工程需求是将安装入户的智能主机接入云端服务器，并通过远程可以进入智能主机进行管理。 最简单方法采用ssh 通过公网ip的服务器实现反向代理。
管理员通过代理ip:port远程访问到智能主机的telnet端口23
``` bash 
AUTOSSH_POLL=60
/usr/sbin/autossh -M 31001 -fCNR 127.0.0.1:41001:0.0.0.0:23 watcher@s0.wall.com  -o TCPKeepAlive=yes -o ServerAliveInterval=30
格式: 
  ip_a:port_a:ip_b:port_b user@remote-server
  在remote-server将 远端 ip_a的port_a端口映射到  本地的 ip_b主机的port_b端口。 
  ip_a 可以是 remote-server 也可以是 remote-server可达的主机ip
  同样，ip_b也可以是本地地址或本地可访达的主机 ip
  
```

- `-M` 链接状态监控端口，用于断线重连

- `-fCNR` 后台运行(f) , 压缩(C),R(反向) 在`s0`主机映射服务器`41001`端口到本地的`23`端口，实现透传。 

