

#判别是否stdin 有可读数据
if select.select([sys.stdin, ], [], [], 0.0)[0]:
    print "Have data!"
    for line in sys.stdin:
        print line
    print 'end'
else:
    print "No data"

"""
def check_method_2():
    if not sys.stdin.isatty():      # isatty() -> bool.  True if the file is connected to a TTY device.
        print "Have data!"
        for line in sys.stdin:
            print line
        print 'end'
    else:
        print "No data"

"""
