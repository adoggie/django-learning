
## 车辆监控系统运行配置 
**Teresa & Rihnocerose**

进入virtualenv环境

source /home/scott/py2.7/bin/active

python 安装相关包 
----
```
celery
xpinyin
qpid-tools
qpid-python
pykafka
gevent
```

初始化表 
------
```
export  PYTHONPATH=/home/docker/rhino_0.2.3/rhino/libs
cd /home/docker/rhino_0.2.3/rhino/services/DataAggregator/src/service
python create_day_table.py
```

服务运行
-------
bash ./start-xxxxx.sh front 

服务配置
---------
```
redis:  26079  密码: 139xxxx 
qpid: 25672
pgsql: 25432  密码: 139xxxx 

locuserservice:  15000 
tracer: 15003 
teresa: 5555 
```

执行一次认证，添加车辆列表到redis
------
http://wallizard.com:15000/rhino/auth/tickets?app_id=teresa&secret_key=57a6a0811829faf34a78ca625c383ec9&user_id=admin&user_roles=root

redis 注释掉 bind 端口，使其对外开放

修改docker 时钟时区
-------
centos7 的docker image 默认采用utc时钟，而rhinoceros所有系统均采用cst时钟(gmt+8)。 
更改utc为cst: 
```
cat /usr/share/zoneinfo/Asia/Shanghai > /etc/localtime 
```

