class Person(object):
    def __init__(self, name, ids):
        self.name = name
        self.ids = ids

    def printSelf(self):
        print '[name: %s, id: %s]' % (self.name, self.ids)


p = Person('Simon', '2308***0317')
p.printSelf()
