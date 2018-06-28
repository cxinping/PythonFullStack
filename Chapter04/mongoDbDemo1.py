# -*- coding: utf-8 -*-
from pymongo import MongoClient
from bson.objectid import ObjectId

#conn = MongoClient('192.168.1.9',27017)
conn = MongoClient('mongodb://192.168.1.9:27017/')

db = conn.mydb
# 插入一条文档
#rs =db.users.insert({"name":'xinping','province':'北京','age':25})
#print('user insert:{0}'.format(rs))

#插入多条文档
'''
rs = db.users.insert([
    {"name":'user1','province': '天津', 'age' : 25},
    {"name":'user2','province': '北京','age' : 24},
    {"name":'user3','province': '哈尔滨', 'age' : 25}
])
print('Multiple users: {0}'.format(rs ))
'''

#查询一条文档
#rs = db.users.find_one({"name" : "user1"})
#rs = db.users.find_one({'age':{"$lt":25}})
#print(rs)
#print('name={0} ,province={1} ,age={2}'.format(rs['name'],rs['province'],rs['age']))

#查询多条文档
'''
for item in db.users.find({"age" : 25 }):
    print(item)
'''

#条件查询
#count = db.users.find({"age":{"$lt":25}} ).count()
#print('count={0}'.format(count))

# 根据_id查询记录
#rs = db.users.find_one({'_id':ObjectId('5b35214d1ec3b721f00d31fc')})
#print(rs)

# 结果排序
'''
for item in db.users.find().sort("age"):
    print(item)

import pymongo
for item in db.users.find().sort("age", pymongo.ASCENDING):
    print(item)
'''

# 更新文档
#rs = db.users.update({'_id':ObjectId('5b3521a61ec3b71cb42b8ee5')},{'$set':{'name':'张三'}})
#print(rs)

# 删除文档
#db.users.remove({'name':'张三'})
db.users.remove()
