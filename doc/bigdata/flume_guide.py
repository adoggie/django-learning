
"""

http://flume.apache.org/releases/content/1.6.0/FlumeUserGuide.html

source,sink,channel 
  source - 接收消息源
  channel - 暂存数据的方式 
  sink - 发送消息目标 

kafka需要配置zookeeper，配置flume读取kafka消息时必须把 zookeeper-3.4.6.jar 拷贝到${FLUME_HOME}/lib下面
或者 配置 FLUME_CLASSPATH=”zookeeper jar 的地址，例如：FLUME_CLASSPATH="/opt/zookeeper/zookeeper-3.4.6.jar"

"""

"""
kafka -> flume -> hdfs 
flume -> kafka -> flume -> hdfs 


"""

"""
配置 kafka 消息存储到 hdfs

kafka-hdfs.sources = kafka-src
kafka-hdfs.channels = file-channel
kafka-hdfs.sinks = hdfs-sink

kafka-hdfs.sinks.hdfs-sink.type = hdfs 
kafka-hdfs.sinks.hdfs-sink.hdfs.path=hdfs://master.grid:9000/data/kafka/%y-%m-%d/%H%M  
#每小时每分钟产生一个日志存储文件

kafka-hdfs.sinks.hdfs-sink.hdfs.path=hdfs://master.grid:9000/data/kafka/%y-%m-%d/%H%M  
kafka-hdfs.sinks.hdfs-sink.hdfs.path=hdfs://master.grid:9000/data/kafka/%y-%m-%d/%H%M  
kafka-hdfs.sinks.hdfs-sink.hdfs.filePrefix = events-
kafka-hdfs.sinks.hdfs-sink.hdfs.round = true
kafka-hdfs.sinks.hdfs-sink.hdfs.writeFormat=TEXT
kafka-hdfs.sinks.hdfs-sink.channel = file-channel
kafka-hdfs.sinks.hdfs-sink.hdfs.fileType = DataStream


kafka-hdfs.channels.file-channel.type=file
kafka-hdfs.channels.file-channel.checkpointDir=/home/grid/flume/temp
kafka-hdfs.channels.file-channel.dataDirs=/home/grid/flume/data

kafka-hdfs.sources.kafka-src.type =org.apache.flume.source.kafka.KafkaSource
kafka-hdfs.sources.kafka-src.channels = file-channel
kafka-hdfs.sources.kafka-src.zookeeperConnect = master.grid:2181
kafka-hdfs.sources.kafka-src.topic = test1-2
kafka-hdfs.sources.kafka-src.groupId = abc
kafka-hdfs.sources.kafka-src.kafka.consumer.timeout.ms = 100

运行： 
flume-ng agent -n kafka-hdfs -c conf -f conf/flume-conf.properties -Dflume.root.logger=DEBUG,console


"""

