aList = [123, 'abc', 4.56, ['inner', 'list'], 7-9j]
print aList

print list('foo')

print aList[0], '--', aList[1:4], '--', aList[:3], '--', aList[1:]

print type(aList[2])

aList[1] = 'Hello World'

print aList

del aList[0]

print aList

sList = ["They", "stamp", "them", 'when', "they're", 'small']

print sorted(sList)
print sList.reverse()

# for t in reversed(sList):
#     print t

for i, s in enumerate(sList):
    print i, '--', s

fn = ['ian', 'stuart', 'david']
ln = ['bairnson', 'elliott', 'paton']

for i, j in zip(fn, ln):
    print ('%s %s' % (i, j)).title()

print sum([1, 3, 5, 7, 9])
print sum([1., 3, 5., 7, 9])

sList.insert(1, 'Simon')
print sList

