# -*- coding: utf-8 -*-

import redis

# 单连接
r = redis.Redis(host='127.0.0.1', port=6379, db=0)

# 连接池
#pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
#r = redis.Redis(connection_pool=pool)

r.set('name', 'xinping')
print( r.get('name'))








