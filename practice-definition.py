# coding=utf-8


class RoundFloat(object):
    def __init__(self, val):
        assert isinstance(val, float), 'Value must be a float'
        self.val = val

    # 相当于toString()方法
    def __str__(self):
        return 'RoundFloat[val=%s]' % self.val


f = RoundFloat(100.0)
print f.val
print f

# f = RoundFloat(100)
# print f.val


class Time60(object):
    def __init__(self, hr, min):
        self.hr = hr
        self.min = min

    def __str__(self):
        return '%d:%d' % (self.hr, self.min)

    # '+'算数符重载
    def __add__(self, other):
        return self.__class__(self.hr + other.hr, self.min + other.min)

    # '+='算数符重载
    def __iadd__(self, other):
        self.hr += other.hr
        self.min += other.min
        return self


mon = Time60(10, 30)
tue = Time60(11, 15)

print mon
print tue
print mon + tue
mon += tue
print mon
