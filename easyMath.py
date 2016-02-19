# coding=gbk

from operator import add, sub
from random import randint, choice

ops = {'+': add, '-': sub}
MAXTRIES = 2


def doprob():
    # ������ط����ַ����е�һ��
    op = choice('+-')

    # randint(), ���������
    nums = [randint(1, 10) for i in range(2)]
    nums.sort(reverse=True)

    # �б�ǰ����Ǻ�, �����ǽ��б�⿪�����������Ĳ��������뺯��.
    # �������Ƶ��������Ǻţ��ǽ��ֵ�⿪�ɶ�����Ԫ����Ϊ�β�.
    # l = [3, 4]
    # add(*l) equals add(3, 4)
    # d = ['a': 3, 'b': 4]
    # add(**d) equals add(3, 4)
    ans = ops[op](*nums)
    pr = '%d %s %d = ' % (nums[0], op, nums[1])
    oops = 0
    while True:
        try:
            if int(raw_input(pr)) == ans:
                print 'correct'
                break

            if oops == MAXTRIES:
                print 'answer\n %s%d' % (pr, ans)
            else:
                print 'incorrect... try again'
                oops += 1
        except (KeyboardInterrupt, EOFError, ValueError):
            print 'invalid input...try again'


def main():
    while True:
        doprob()
        try:
            opt = raw_input('Again? [y]').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == '__main__':
    main()
