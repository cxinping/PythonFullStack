# -*- coding: utf-8 -*-

import csv

with open('test2.csv' ,'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['a','b', 'c'] )
    writer.writerow([1,2,3] )
    writer.writerow([4,5,6] )
