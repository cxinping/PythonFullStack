# -*- coding: utf-8 -*-

def Fibs(max):
    #定义斐波那契数列初始的2个值
    a = 1
    b = 1
    count = 0

    while True:

        if count == max:
            raise StopIteration

        yield a
        a, b = b, a + b
        count = count + 1

if __name__  == "__main__":
    fib = Fibs(5)

    for item in fib:
        print(item)