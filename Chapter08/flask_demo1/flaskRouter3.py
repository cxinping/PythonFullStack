# -*- coding: utf-8 -*-

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg  = ''
    if request.method == 'POST':
        msg = '响应post请求'
    else:
        msg = '响应get请求'
    return msg

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
