
download & install
=========
http://kafka.apache.org/downloads
 

启动zookeeper and kafka-server
"""
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties

ports:
  zookeeper 2181 
  kafka 

 -- partitions 数量必须大于 consumer数量 
 -- 多个 consumer group 实现多播 ； consumer group中多个consumer实现单播
 
 一个topic分布在broker上存在1个或多个partition, consumer读取1个或多个partition的数据，不同partition的数据不能保持先后顺序，同一个partition的数据能
 保证读取的先后次序。
 
 


创建topic
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test 
 查看topic
 bin/kafka-topics.sh --list --zookeeper localhost:2181
./kafka-topics.sh --describe --topic test --zookeeper localhost:2181  

发送消息
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test
 
 接收消息
 bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic test --from-beginning
 
 修改 server.properties
      listeners=PLAINTEXT://localhost:9092  
  
  
 彻底删除topic：
 1.删除kafka存储目录（server.properties文件log.dirs配置，默认为"/tmp/kafka-logs"）相关topic目录
 2.如果配置了delete.topic.enable=true直接通过命令删除，如果命令删除不掉，直接通过zookeeper-client 删除掉broker下的topic即可。
 标记为marked for deletion的topic你可以在zookeeper客户端中通过命令获得：ls /admin/delete_topics/【topic name】
 
 """

"""
master/slave模式用于备份和主备服务，通过监听服务节点的变动，来设置那些slave节点为master节点。 （最小序号、选举法)
一个partition对应一个consumer ，一个consumer组group内多个consumer可以实现负载均衡，多个group内的consumer实现广播接收。 

producer直接连接broker发布消息，consumer连接zookeeper读取消息。 

pykafka : 
   http://pykafka.readthedocs.org/

simple_consumer / balanced_consumer 

  cs = tp.get_balanced_consumer(
   consumer_group='abc',
   auto_commit_enable=True,
   zookeeper_connect='192.168.199.41:2181'
  )
  
  balanced_consumer用于负载均衡，多个kafka客户依次读取同一个topic的消息，partition的数量必须大于topic的读取用户数量。 
  balanced读取方式必须指定相同的group名称，如果group不同，则topic消息被广播到读取客户。 
  
  当topic的partition数量小于消息读取者时，后者读取进程将顶掉前者读取进程的连接。 
  

"""
  
   
   
  
  
