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
    data = {
        '华为':math.ceil(random.random() * 100),
        '小米':math.ceil(random.random() * 100),
        'oppo': math.ceil(random.random() * 100)
        }
    msg_dict = {'msg': data}
    msg_jsonstr = json.dumps(msg_dict)
    return msg_jsonstr

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
