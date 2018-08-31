# -*- coding: utf-8 -*-

def mygen():
    print('gen() 1')
    yield 1

    print('gen() 2')
    yield 2

    print('gen() 3')
    yield 3


gen = mygen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))