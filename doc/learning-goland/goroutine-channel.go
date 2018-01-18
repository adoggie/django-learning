

channel可视为两个传统thread之间数据交互的队列(queue) 

定义队列对象
ch:=make(chan int) 声明此队列数据类型为int，默认是非缓存unbuffer类型


a<-ch  读取队列数据
ch<-a  写入队列数据

channel的几个基本操作:  send,recv,close

非缓存队列 unbuffered channel 
队列发送者发送消息到ch队列，一直等待消息被读取，这种方式成为同步队列synchronized channel 
在应用中，启动goroutine并等待其结束相当简单

wait:=make(chan int)
go func(){
   ...
   wait<-0
}
<-wait   //等待routine运行结束返回消息

channel应用在不同goroutine之间进行消息的传递 
go routine-1: ch<-a
go routine-2: b<-ch
routine1充当消息生产者，将消息发送到ch，routine2充当消费者，从ch读取消息



