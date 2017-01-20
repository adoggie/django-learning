
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
  
   
   
  
  
