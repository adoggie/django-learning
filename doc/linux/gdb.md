
gdb 调试忽略信号SIGUSR1

handle SIGUSR1 nostop


~/.gdbinit
handle SIGUSR1 nostop noignore noprint
handle SIG34 nostop noignore noprint
