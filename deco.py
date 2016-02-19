from time import ctime, sleep

def tsfunc(func):
    def wrappedFunc():
        print '[%s] %s() called' % (ctime(), func.__name__)
        func()
        return func
    return wrappedFunc

@tsfunc
def foo():
    # print 'foo()'
    pass

for i in range(3):
    foo()
    sleep(1)
