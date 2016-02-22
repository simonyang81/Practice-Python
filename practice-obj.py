# coding=utf-8
class Person(object):
    """this is a person class"""

    # 类的静态成员
    version = 1.1

    def __init__(self, name, ids):
        self.name = name
        self.ids = ids

    def printSelf(self):
        print '[name: %s, id: %s]' % (self.name, self.ids)


p = Person('Simon', '2308***0317')
p.printSelf()

print p.version
print Person.version

Person.version = 1.3

print p.version
print Person.version

print "class name is %s" % Person.__name__
print 'Docs: ', Person.__doc__
print Person.__bases__
print Person.__dict__
print 'Person module:', Person.__module__

print p.__class__
