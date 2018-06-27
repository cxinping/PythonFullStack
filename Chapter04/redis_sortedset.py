# -*- coding: utf-8 -*-

import redis
pool = redis.ConnectionPool(host='127.0.0.1', port=6379,db=0 )
r = redis.Redis(connection_pool=pool)

#1
print('\n#1')
r.zadd('zset1',num1=1,num2=2,num3=3)

#2
print('\n#2')
r.delete('zset1')
r.zadd('zset1',num1=1, num2=2, num3=3, num4=4)
print(r.zcard('zset1'))

#3
print('\n#3')
r.delete('zset1')
r.zadd('zset1',num1=1, num2=2, num3=3, num4=4)
print(r.zrange('zset1',0,-1))

#4
print('\n#4')
r.delete('zset1')
r.zadd('zset1',num1=1, num2=2, num3=3, num4=4)
r.zrem('zset1','num1', 'num2', 'num3')

#5
print('\n#5')
r.delete('zset1')
r.zadd('zset1',num1=1, num2=2, num3=3, num4=4)
print( r.zscore('zset1' , 'num2') )






















