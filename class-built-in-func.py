class C1(object):
    pass


class C2(object):
    pass


class GC(C1):
    pass


c1 = C1()
c2 = C2()

print 'c1 is instance C1 == ', isinstance(c1, C1)
print 'c2 is instance C1 == ', isinstance(c2, C1)
print 'c1 is instance C2 == ', isinstance(c1, C2)
print 'c2 is instance C2 == ', isinstance(c2, C2)

print 'GC is subclass C2 ==', issubclass(GC, C2)
print 'GC is subclass C1 ==', issubclass(GC, C1)
print 'C1 is subclass C2 ==', issubclass(C1, C2)