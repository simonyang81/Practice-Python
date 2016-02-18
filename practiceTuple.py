aTuple = (123, 'abc', 4.56, ['inner', 'tuple'], 7-9j)

print aTuple

print aTuple[0], '--', aTuple[1]

print(aTuple[1:4])

print '123 in aTuple == %s' % (123 in aTuple)
print "'123' in aTuple == %s" % ('123' in aTuple)
print "'abc' in aTuple == %s" % ('abc' in aTuple)

aList = list(aTuple)
aList.insert(1, 456)
print aList

t = ('first', 'second')
print t
t += ('third', 'fourth')
print t
