
采用Clion进行Debug时，程序会接收到不同的信号  SIGUSR1 SIGPIPE 等，导致程序终止被退出。 

发现对GDB调试参数设置即可

```
vim ~/.gdbinit
handle SIGUSR1 noprint nostop

```

Mac下Clion采用 clang 编译器 则无次问题

