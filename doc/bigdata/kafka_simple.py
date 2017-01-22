
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
  
  
 彻底删除topic：
 1.删除kafka存储目录（server.properties文件log.dirs配置，默认为"/tmp/kafka-logs"）相关topic目录
 2.如果配置了delete.topic.enable=true直接通过命令删除，如果命令删除不掉，直接通过zookeeper-client 删除掉broker下的topic即可。
 标记为marked for deletion的topic你可以在zookeeper客户端中通过命令获得：ls /admin/delete_topics/【topic name】
 
 """

"""
master/slave模式用于备份和主备服务，通过监听服务节点的变动，来设置那些slave节点为master节点。 （最小序号、选举法)
一个partition对应一个consumer ，一个consumer组group内多个consumer可以实现负载均衡，多个group内的consumer实现广播接收。 

producer直接连接broker发布消息，consumer连接zookeeper读取消息。 

"""
  
   
   
  
  
