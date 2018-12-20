# -*- coding: utf-8 -*-
from flask import Flask,request
import json
import math
import random

app = Flask(__name__, static_url_path='', static_folder='')

@app.route('/')
def index():
    return 'flask server'

@app.route('/getdata', methods=['GET', 'POST'])
def getdata():
    # 生成三个厂商的手机销量数据，数据类型是字典
    data = {
        '华为': math.ceil(random.random() * 100),
        '小米': math.ceil(random.random() * 100),
        'oppo': math.ceil(random.random() * 100)
    }
    msg_dict = {'msg': data }
    # 转换数据，从字典类型转换为字符串
    msg_jsonstr = json.dumps(msg_dict)
    return msg_jsonstr

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

# http://127.0.0.1/index.html