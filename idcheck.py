# coding=gbk
# 标识符合法性检查,首先要以字母或者下划线开始,后面要跟字母,下划线或者数字.
# 这个小例子只检查长度大于等于2的标识符

import string

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'

while True:
    myInput = raw_input('Identifier to test?')

    if len(myInput) > 1:
        if myInput[0] not in alphas:
            print ''' invalid: first symbol must be alphabetic '''
        else:
            for otherChar in myInput[1:]:
                if otherChar not in alphas + nums:
                    print ''' invalid: remaining symbols must be alphanumeric '''
                    break
                else:
                    print 'okay as an identifier'
                    break
    elif len(myInput) == 1:
        if myInput[0] in string.letters:
            print 'okay as an identifier'
        else:
            print ''' invalid: first symbol must be alphabetic '''
