# -*- coding: utf-8 -*-

import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

#1
print('\n#1')
r.sadd('sets', 1,2,3,4)

#2
print('\n#2')
r.delete('sets')
r.sadd('sets', 1,2,3,4)
print( r.scard('sets') )

#3
print('\n#3')
r.delete('sets')
r.sadd('sets', 1,2,3,4)
print( r.smembers('sets') )
print(  type( r.smembers('sets') ) )

#4
print('\n#4')
r.delete('sets1')
r.delete('sets2')
r.sadd('sets1', 1,2,3)
r.sadd('sets2', 2,3,4)
print( r.sdiff('sets1', 'sets2') )

#5
print('\n#5')
r.delete('sets1')
r.delete('sets2')
r.sadd('sets1', 1,2,3)
r.sadd('sets2', 2,3,4)
print( r.sinter('sets1', 'sets2') )

#6
print('\n#6')
r.delete('sets1')
r.delete('sets2')
r.sadd('sets1', 1,2,3)
r.sadd('sets2', 2,3,4)
print( r.sunion('sets1', 'sets2') )

















