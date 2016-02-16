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

# �ѵ�һ���ַ�ת�ɴ�д
print 'hello world'.capitalize()

# ����һ��ԭ�ַ�������, ��ʹ�ÿո����������width�����ַ���
print '-' + 'hello world'.center(20) + '-'

# string.count(str, start, end), ����str��string����ֵĴ���, ���start����endָ��, �򷵻�ָ����Χ�ڵ�
print 'hello world'.count('l')

# ����ַ����Ƿ���obj����
print 'hello world'.endswith('ld')

# string.find(str), ���str�Ƿ������string��, ����Ƿ��ؿ�ʼ������ֵ, ���򷵻�-1
t = Template('\'e\' index \'${idx}\' in hello world')
print t.safe_substitute(idx='hello world'.find('e'))

# ���string������һ���ַ����������ַ�������ĸ�������򷵻�True, ���򷵻�False
print '\'123\' is alnum ==', '123'.isalnum()

# string.join(seq), ��string��Ϊ�ָ���, ��seq�����е�Ԫ��(�ַ���)��ʾ�ϲ�Ϊһ���µ��ַ���
print ':'.join('hello world')

# ת�����д�д�ַ�ΪСд
print 'HELLO WORLD'.lower()

# ȥ����ߵĿո�
print '\'' + '    hello world     '.lstrip() + '\''

# ȥ���ұߵĿո�
print '\'' + '    hello world     '.rstrip() + '\''

# �滻�ַ���, ���numָ��, ���滻����������num
print 'hello world'.replace('world', 'simon')

# ����find, �����ǲ������һ�����ֵ��ַ�
print 'hello world'.rfind('o')

# ����ַ����Ƿ���obj��ͷ
print 'hello world'.startswith('hl')

# ��ת�ַ�����Сд
print 'hELLO wORLD'.swapcase()