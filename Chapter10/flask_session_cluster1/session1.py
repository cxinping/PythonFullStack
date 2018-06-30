# -*- coding: utf-8 -*-
from flask import Flask, session, request, redirect
from flask_session import Session
from redis import Redis

app = Flask(__name__, static_url_path='', static_folder='')
# 设置session需要设置秘钥
app.secret_key = '123456'

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = Redis(host='127.0.0.1',port='6379')
Session(app)

@app.route("/index")
def index():
    sessionId = request.cookies.get('session')
    username = session['username']
    return '<br/>sessionId={0}<br/> username={1}, webserver1'.format(sessionId,username)

@app.route("/login", methods=['POST'])
def login():
    session['username'] = request.form['username']
    return redirect('/index')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8081)

# http://127.0.0.1:8081/index.html