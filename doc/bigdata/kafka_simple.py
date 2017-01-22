
启动zookeeper and kafka-server
"""
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties


创建topic
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test 
 查看topic
 bin/kafka-topics.sh --list --zookeeper localhost:2181
  
发送消息
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test
 
 接收消息
 bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic test --from-beginning
 
 修改 server.properties
      listeners=PLAINTEXT://localhost:9092  
   
 """

"""
master/slave模式用于备份和主备服务，通过监听服务节点的变动，来设置那些slave节点为master节点。 （最小序号、选举法)
一个partition对应一个consumer ，一个consumer组group内多个consumer可以实现负载均衡，多个group内的consumer实现广播接收。 

producer直接连接broker发布消息，consumer连接zookeeper读取消息。 

"""
  
   
   
  
  
