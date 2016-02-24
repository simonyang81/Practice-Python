# coding=utf-8


class P1(object):
    def foo(self):
        print 'P1 class -> foo()'


class P2(object):
    def foo(self):
        print 'P2 class -> foo()'

    def bar(self):
        print 'P2 class -> bar()'


class C1(P1, P2):
    def foo(self):
        super(C1, self).foo()
        print 'C1 class -> foo()'


class C2(P2, P1):
    def foo(self):
        super(C2, self).foo()
        print 'C2 class -> foo()'


c1 = C1()
c1.foo()

c2 = C2()
c2.foo()
