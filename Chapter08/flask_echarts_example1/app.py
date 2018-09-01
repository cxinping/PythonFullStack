# -*- coding: utf-8 -*-
import cpuDao as cpuDao
from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_url_path='', static_folder='')

@ app.route('/cpu', methods=['GET', 'POST'])
def cpu():
    if request.method == "GET":
        res = cpuDao.query_db("SELECT * FROM cpu WHERE id <= 6")  # 第一次只返回6个数据
    elif request.method == "POST":
        res = cpuDao.query_db("SELECT * FROM cpu WHERE id = (%s)", args=(int(request.form['id']) + 1,))  # 以后每次返回1个数据

    print(res)

    # 返回json格式
    return jsonify(insert_time = [x[1] for x in res],
                   cpu1 = [x[2] for x in res],
                   cpu2 = [x[3] for x in res],
                   cpu3 = [x[4] for x in res],
                   cpu4 = [x[5] for x in res])

@ app.route('/')
def index():
    return '<a href="http://www.baidu.com">baidu</a>'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
