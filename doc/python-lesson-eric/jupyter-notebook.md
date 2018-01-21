
登录notebook
```
http://wallizard.com:8888/

passwd: eric's birthday
```

运行notebook
```sh
su - zyc 

source pyenv/bin/active    切换到 pyevn环境
jupyter notebook --ip=106.14.82.12  启动notebook

配置文件
[.jupyter]  存放notebook的配置和密码

```

修改登录密码
```python
from notebook.auth import passwd
passwd()

```

