# -*- coding: utf-8 -*-

import csv

with open('test.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        # 返回列表对象
        print(row)