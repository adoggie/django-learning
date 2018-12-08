

## 环境 
 
 * ubuntu 14.4  32位 真机或者docker
 * 安装 gcc 
 * 交叉工具  arm-linux-gnueabihf , gcc-4.7.3 
 
## 主要说明 

 python编译分x86环境和交叉编译环境两个步骤
 
 1. 下载 Python-2.7.3.tar.gz  

``` 
  tar xvzf Python-2.7.3.tar.gz 
  mv Python-2.7.3 Python-2.7.3.orig 
  
```
 
 2. x86编译

```
    cp -p files/config.site Python-2.7.3.orig
    ./configure  CONFIG_SITE="config.site" --prefix=/smart/arm32/root
    
    make python.exe Parser/pgen 
    mv python hostpython
    mv Parser/pgen Parser/hostpgen
    make  distclean
    patch -p0 < ./files/Python-2.7.3-xcompile.patch  打补丁
```
编译完成会生成  python.exe x86的程序文件

3. 交叉环境

设置环境变量：
```
export PATH=$PATH:/smart/arm-linux-gcc/bin/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games
export SYSROOT=/smart/arm-linux-gcc/arm-linux-gnueabihf/libc/usr/
export CC=arm-linux-gnueabihf-gcc
export CXX=arm-linux-gnueabihf-g++
export AR=arm-linux-gnueabihf-ar
export RANLIB=arm-linux-gnueabihf-ranlib
#export LD=arm-linux-gnueabihf-ld
#export LDFLAGS=-L/smart/arm-linux-gcc/arm-linux-gnueabihf/libc/usr/lib/arm-linux-gnueabi
export PS1="\[\e[32;1m\][linux-devkit]\[\e[0m\]:\w> "

```

支持sqlite 

```
(修改 setup.py)
mydir = os.environ.get('PYTHON_XCOMPILE_DEPENDENCIES_PREFIX')
            if mydir:
                inc_dirs += [mydir + '/include' ]
                inc_dirs += [mydir + '/lib/libffi-3.0.10/include']
                inc_dirs += ['/smart/arm32/root/include']
                lib_dirs += [mydir + '/lib' ]
                lib_dirs += ['/smart/arm32/root/lib’ ]
                
见 setup.py 
```

运行 build-2.sh

运行 build-3.sh


```
  cd Python2.7.3.orig
  make install 
```

4. arm 运行

拷贝 /smart/arm32/root 到 arm 设备 /home/local/root下 。

设置环境变量：

```
export PYTHONPATH=/home/local/root/lib/python2.7:/home/local/root/lib/python2.7/lib-dynload:/home/local/root/lib/python2.7/site-packages/
export LD_LIBRARY_PATH=/home/local/root/lib
export PATH=/home/local/root/bin:$PATH

```

 
