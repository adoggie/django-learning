
python简介

版本 www.python.org  2.7.x / 3.5.x 
特点、应用场景

'''
高级的、面向对象的、可扩展的、可移植的、易于学习和维护的程序语言
动态语言，程序在运行时可以动态修改对象元数据
弱类型语言，数据由 标量scalar和容器container 表示 ，GC进行内存资源管理
一种胶水语言，依赖第三方软件包，用于业务逻辑的编写和模块的组合 
适用 快速交付、原型建模，自动化运维 。。 
结合第三方软件包，具有强大的功能，适应于场景： 网络通信、UI、WebService、分布式计算和存储..
除了OS和Driver，几乎没有不能做的！
灵活和松散的特性，入门容易，精通难，坑很多，步步惊心！
'''

相关项目 
  django，pyqt numpy goagent openstack 豆瓣 spark boost pycrypto pil xlws
  
实现版本 cpython

安装 pip 市场pypi download
  wget https://bootstrap.pypa.io/get-pip.py
    

运行 idel，ipython，pycharm os运行差异
   ipython cmd(? ?? *  %run cmd ) 
   ipython qtconsole --pylab=inline
   pip install qtconsole 
   ipython --pylab
    ipython notebook
   最近的两个输出结果保存在_(一个下划线)和__(两个下划线)变量中
   !cmd 执行系统命令
               
帮助系统 pydoc

文件形式: py pyc pyo pyw pyd

语法介绍   
helloworld

面向过程和对象  内建函数 模块级函数 类级函数 对象函数

关键字 
False      class        finally      is           return
None     continue     for          lambda       try
True       def          from         nonlocal     while
and        del          global       not          with
as           elif         if           or           yield
assert     else         import       pass
break     except       in           raise 

from import as  _main_ dir 包管理 _init.py_

文档缩进 注释

数值类型 int long float complex
布尔 True False
字符串 单双引号
None 

数值运算 逻辑运算 位操作

字符串操作相关函数 *

数组 list与tuple 范围取值 数组操作函数 len range crud

字典dict  k=v items keys values crud

if else pass
for while in 

def 默认参数 *args **kvargs def内嵌
lambda map reduce sort

try except finally
class self inherit super @staticmethod object
has_attr set_attr

对象内建函数 init getitem str
重载： http://www.cnblogs.com/wjoyxt/p/5112537.html
  
数据库访问 
    dbi https://www.python.org/dev/peps/pep-0249/
    psycopg  http://initd.org/psycopg/
      conn = psycopg2.connect(dbname,user, password)
      cusor
      to see : http://www.cnblogs.com/yy3b2007com/p/5724427.html
    sqlite3
      http://www.runoob.com/sqlite/sqlite-python.html
      connect(path) connect("memory:")
    
docstring helpdoc
  sphinx : yum install python-sphinx     sphinx-quickstart
  pyment: https://github.com/dadadel/pyment   
        pyment test.py   patch -p1 < test.py.patch
  doxygen http://www.stack.nl/~dimitri/doxygen/
  pdoc https://github.com/BurntSushi/pdoc

装饰器@decorderator
内存管理 gc None 引用计数 deepcopy

相关函数
  dir type id list tuple open str hex int map reduce list zip

相关模块
  os sys os.path time socket json urllib struct pickle sqlite re threading stringIO logging unittest

项目介绍
ctypes  https://github.com/adoggie/py-ffmpeg/blob/master/ffmpeg.py
pyqt   https://github.com/adoggie/vlc_player/blob/master/video_player.pyw
gevent
django
numpy
scrapy
py4j - 实现python与java之间互相调用 
pyjnius - python调用java类，据说优于py4j，目前没感觉到！
chardet - 字符集检测  
  "iconv -f GB2312 -t UTF-8 xxx.txt "  " chardetect.py xxx.txt"
paramiko - ssh 自动化
pykafka
zkpython 
pysal  - 地理空间计算库 
numpy  - 数值计算
scipy -  数值计算
celery - 异步rpc
pep8.py - 代码规格检查
pydot / pygraphviz / networkx / osg (社交网络有向图) http://networkx.github.io
matplotlib.pyplot
pyexcept
poster / requests (http client)
Docutils  rst格式转换
Pygments  代码语法高亮
objgraph/pygraph  绘制有向图  objgraph.show_refs([c],filename='/tmp/test.png')

mysql-connector   https://github.com/sanpingz/mysql-connector

微服务
--------
connexion    - "https://pypi.python.org/pypi/connexion  基于配置的微型service app， 基本实现功能在djangoframework中都覆盖了。 "
  
