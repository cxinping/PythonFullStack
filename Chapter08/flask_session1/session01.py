# -*- coding: utf-8 -*-
from flask import Flask, session, request

app = Flask(__name__, static_url_path='', static_folder='')
# 设置session需要设置秘钥
app.secret_key = '123456'
# 设置session过期时间，单位：秒
app.config['PERMANENT_SESSION_LIFETIME'] = 20

@app.route("/get/")
def get():
    if 'username' in session:
        return 'hello, {0}\n'.format(session['username'])
    return 'hello, stranger\n'

@app.route("/login", methods=['POST'])
def login():
    session['username'] = request.form['username']
    print( 'session => ',request.cookies.get('session') )

    return 'login success'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)


# http://127.0.0.1/static/index.html