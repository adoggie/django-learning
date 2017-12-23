
## 描述:
朋友的游戏项目后台对接apple的消息推送，采用python相关开发组件实现，期间碰到python版本ssl不适配的问题。 

**系统环境**
```
centos 7.4 
python 2.7.5 
django 1.6.8 
gevent 1.2 
psycopg2
uwsgi
requests
psycogreen
redis
PyYAML
python-dateutil
django-cors-headers
djangorestframework==3.1.2
IMAGE
pymongo
```

对接apple推送相关python包
```
hyper 
apns2   (easy_install apns2)  https://github.com/Pr0Ger/PyAPNs2 
```

在推送代码中发现系统自带的py2.7.5的ssl版本过低调用apns2时提示协议版本过低，而重新下载编译的2.7.14并无此问题。
为了不影响系统默认的python2.7.5的环境，采用virtualenv的方案部署运行环境. 

### 步骤： 

#### 0.前置条件 
```
确保 zlib-devel , openssl-devel, python-devel 已经安装
```

#### 1. 安装 virtualenv
```sh
pip install virtualenv
```
#### 2. 编译 python2.7.14 
```
mkdir /home/source
cd /home/source 
wget https://www.python.org/ftp/python/2.7.14/Python-2.7.14.tgz 
tar xvzf Python-2.7.14.tgz ; cd Python-2.7.14
./configure ; make ; make install 

编译完成自动安装到 /usr/local/bin/python
```

**注意** 

某些场景编译时会出现不包含 _ssl 模块的情况,那就需要手动修改相关文件。
在 `.configure`之后，修改配置文件`Setup` ,然后再进行 `make ; make install `

```
vim /home/source/Python-2.7.14/Modules/Setup

取消以下几行注释：

# Socket module helper for socket(2)
_socket socketmodule.c timemodule.c

# Socket module helper for SSL support; you must comment out the other
# socket line above, and possibly edit the SSL variable:
#SSL=/usr/local/ssl
_ssl _ssl.c \
-DUSE_SSL -I$(SSL)/include -I$(SSL)/include/openssl \
-L$(SSL)/lib -lssl -lcrypto
```

#### 3. 生成虚拟环境

```sh
mkdir /home/py2714; 
virtualenv -p /usr/local/bin/python /home/py2714 

```

#### 4. 测试virtualenv 

进入虚拟环境安装相关程序包
```
source /home/py2714/bin/activate
pip install hyper 
easy_install apns2
```
#### 5. 完成收工
