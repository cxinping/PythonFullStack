# -*- coding: utf-8 -*-
from pymongo import MongoClient
#conn = MongoClient('192.168.1.9',27017)
conn = MongoClient('mongodb://192.168.1.9:27017/')

db = conn.mydb
#rs =db.users.insert({"name":'xinping','province':'北京','age':25})
#print('user insert:{0}'.format(rs))
