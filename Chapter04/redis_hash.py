# -*- coding: utf-8 -*-

import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

#1
print('\n#1')
r.hset('user','name','xinping')

#2
print('\n#2')
r.hmset('user',{ 'name': 'lisi' ,'age':20 })

#3
print('\n#3')
r.hset('user','name','xinping')
print( r.hget('user', 'name') )

#4
print('\n#4')
r.hmset('user',{ 'name': 'lisi' ,'age':20 })
print( r.hmget('user', ['name', 'age']) )
print( r.hmget('user', 'name', 'age') )
