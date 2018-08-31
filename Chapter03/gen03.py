# -*- coding: utf-8 -*-

# 定义迭代器
class odd(object):

    def __init__(self, max):
        self.count = 0
        self.max = max
        self.start = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 2
        self.count = self.count + 1
        if self.count == self.max:
            raise StopIteration

        return self.start

odd_num = odd(3)
for num in odd_num:
    print(num)
