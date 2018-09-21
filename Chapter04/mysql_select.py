# -*- coding: utf-8 -*-

import pymysql
# 打开数据库连接
db = pymysql.connect(host="127.0.0.1", user="root", password="123456",
                     database="mytestdb", port=3306, charset="utf8")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (2000)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        name = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("id=%s,name=%s,age=%d,sex=%s,income=%d" % \
              (id, name, age, sex, income))
except Exception as e:
    print(e)
finally:
    # 关闭数据库连接
    db.close()
