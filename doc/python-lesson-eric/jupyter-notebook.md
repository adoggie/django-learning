
登录notebook
```
http://wallizard.com:8888/
passwd: 1111
```

运行notebook
```sh
su - zyc 
source pyenv/bin/active    切换到 pyevn环境
jupyter notebook --ip=106.14.82.12 --port=9999 启动notebook
jupyter notebook password 修改密码

配置文件
[.jupyter]  存放notebook的配置和密码
```

修改登录密码
```python
from notebook.auth import passwd
passwd()

```

