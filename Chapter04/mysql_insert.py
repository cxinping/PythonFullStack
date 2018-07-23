# -*- coding: utf-8 -*-

import pymysql
# 打开数据库连接
db = pymysql.connect("127.0.0.1", "root", "123456", "mytestdb",charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO employee(name, age,sex, income) VALUES( '王五1' ,25,'0' , 5000 )"

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except Exception as e:
    # 如果发生错误则回滚
    print(e)
    db.rollback()

# 关闭数据库连接
db.close()
