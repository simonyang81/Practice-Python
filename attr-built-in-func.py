class C1(object):
    def __init__(self):
        self.foo = 100


c = C1()
print 'c has foo attr == ', hasattr(c, 'foo')
print 'c get foo attr == ', getattr(c, 'foo', 0)
print '==>> set c foo attr to 200'
setattr(c, 'foo', 200)
print 'c get foo attr == ', getattr(c, 'foo', 0)
print '==>> delete c foo attr'
delattr(c, 'foo')
print 'c has foo attr == ', hasattr(c, 'foo')
