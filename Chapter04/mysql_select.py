# -*- coding: utf-8 -*-

import pymysql
# 打开数据库连接
db = pymysql.connect("127.0.0.1", "root", "123456", "mytestdb",charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL删除记录语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 向数据库提交
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()
