# coding=gbk

from string import Template

aString = 'Hello World!'

print aString
print 'aString type ==', type(aString)

print '----------------------'

s = str(range(6))
print s

print '----------------------'

print 'aString[:],', aString[6:]

print '----------------------'

print 'H not in aString ==', 'H' not in aString
print 'H in aString ==', 'H' in aString

print '----------------------'

# 把第一个字符转成大写
print 'hello world'.capitalize()

# 返回一个原字符串居中, 并使用空格填充至长度width的新字符串
print '-' + 'hello world'.center(20) + '-'

# string.count(str, start, end), 返回str在string里出现的次数, 如果start或者end指定, 则返回指定范围内的
print 'hello world'.count('l')

# 检查字符串是否以obj结束
print 'hello world'.endswith('ld')

# string.find(str), 检测str是否包含在string中, 如果是返回开始的索引值, 否则返回-1
t = Template('\'e\' index \'${idx}\' in hello world')
print t.safe_substitute(idx='hello world'.find('e'))

# 如果string至少有一个字符并且所有字符都是字母或数字则返回True, 否则返回False
print '\'123\' is alnum ==', '123'.isalnum()

# string.join(seq), 以string作为分隔符, 将seq中所有的元素(字符串)表示合并为一个新的字符串
print ':'.join('hello world')

# 转换所有大写字符为小写
print 'HELLO WORLD'.lower()

# 去掉左边的空格
print '\'' + '    hello world     '.lstrip() + '\''

# 去掉右边的空格
print '\'' + '    hello world     '.rstrip() + '\''

# 替换字符串, 如果num指定, 则替换次数不超过num
print 'hello world'.replace('world', 'simon')

# 类似find, 不过是查找最后一个出现的字符
print 'hello world'.rfind('o')

# 检查字符串是否以obj开头
print 'hello world'.startswith('hl')

# 翻转字符串大小写
print 'hELLO wORLD'.swapcase()