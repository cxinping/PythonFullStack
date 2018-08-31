# -*- coding: utf-8 -*-

def mygen():
    print('gen() 1')
    yield 1  # 返回第一个值

    print('gen() 2')
    yield 2  # 返回第二个值

    print('gen() 3')
    yield 3  # 返回第三个值

gen = mygen()     # 拿到一个生成器
print(next(gen))  # 取第一个值
print(next(gen))  # 取第二个值
print(next(gen))  # 取第三个值
print(next(gen))  #取不存在的第四个值，会抛出StopIteration异常
