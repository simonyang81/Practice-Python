# coding=utf-8

def plus(number):
    # 在函数内部再定义一个函数, 这个里面的函数就被认为是闭包
    def plus_in(number_in):
        print number_in
        return number + number_in
    # 返回闭包的结果
    return plus_in

# 给函数plus赋值, 这个20就是给参数number
v = plus(20)
# 这里的100其实给参数number_in
print v(100)