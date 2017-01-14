
pycharm 运行pyspark程序 
安装 py4j 
在 pytcharm中设置
    PYTHONPATH=$spark/python
    SPARK_HOME=$spark
    
from pyspark import SparkConf, SparkContext 

conf = SparkConf().setMaster("local").setAppName("myApp") 
sc = SparkContext(conf = conf)


"""
-- 统计客户通话记录时长 --

a = sc.textFile('./sjt/a.txt')
b = sc.textFile('./sjt/b.txt')


rs = b.map( lambda s:s.split(',')).\
	filter(lambda x: len(x)>5 ).\
	map(lambda _:(_[0],_[5])).\
	reduceByKey(lambda x,y: int(x)+ int(y) )
rs.saveAsTextFile('result.txt')

"""

