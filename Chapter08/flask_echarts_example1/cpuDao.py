# -*- coding: utf-8 -*-
import pymysql

def saveToDb(*data):
    # 格式化数据
    data = (data[0], data[1][0], data[1][1], data[1][2], data[1][3])
    print(data)
    # 打开数据库连接
    db = pymysql.connect("127.0.0.1", "root", "123456", "mytestdb", charset="utf8")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = 'INSERT INTO cpu(insert_time,cpu1,cpu2,cpu3,cpu4) VALUES ( %s, %s, %s, %s, %s)'
    try:
        # 执行sql语句
        cursor.execute(sql , data)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        print(e)
        # 如果发生错误则回滚
        db.rollback()

    # 关闭数据库连接
    db.close()

def query_db(query, args=(), one=False):
    # 打开数据库连接
    db = pymysql.connect("127.0.0.1", "root", "123456", "mytestdb", charset="utf8")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    try:
        # 执行SQL语句
        print("*** args=> ", args)
        cursor.execute(query, args)
        # 获取所有记录列表
        results = cursor.fetchall()
    except Exception as e:
        print("Error: unable to fetch data", e)

    # 关闭数据库连接
    db.close()
    return results
