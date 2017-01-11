
pycharm 运行pyspark程序 
安装 py4j 
在 pytcharm中设置
    PYTHONPATH=$spark/python
    SPARK_HOME=$spark
    
from pyspark import SparkConf, SparkContext 

conf = SparkConf().setMaster("local").setAppName("myApp") 
sc = SparkContext(conf = conf)
