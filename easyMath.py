# coding=utf-8

from operator import add, sub
from random import randint, choice

ops = {'+': add, '-': sub}
MAXTRIES = 2


def doprob():
    # 随机返回返回字符串中的一个
    op = choice('+-')

    # randint(), 生成随机数
    nums = [randint(1, 10) for i in range(2)]
    nums.sort(reverse=True)

    # 列表前面加星号, 作用是将列表解开成两个独立的参数，传入函数.
    # 还有类似的有两个星号，是将字典解开成独立的元素作为形参.
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
