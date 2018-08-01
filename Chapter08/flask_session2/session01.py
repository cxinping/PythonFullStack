# -*- coding: utf-8 -*-
from flask import Flask, session, request
from flask_session import Session
from redis import Redis

app = Flask(__name__, static_url_path='', static_folder='')
# 设置session需要设置秘钥
app.secret_key = '123456'

app.config['SESSION_TYPE'] = 'redis'  # session类型为redis
app.config['SESSION_PERMANENT'] = False  # 如果设置为True，则关闭浏览器session就失效。
app.config['SESSION_USE_SIGNER'] = False  # 是否对发送到浏览器上session的cookie值进行加密
app.config['SESSION_KEY_PREFIX'] = 'session:'  # 保存到session中的值的前缀
app.config['SESSION_REDIS'] = Redis(host='127.0.0.1', port='6379' )  # 用于连接redis的配置
Session(app)

# 获取session
@app.route("/get/")
def get():
    if 'username' in session:
        return 'hello, {0}\n'.format(session['username'])
    return 'hello, stranger\n'

# 保存会话
@app.route("/login", methods=['POST'])
def login():
    session['username'] = request.form['username']
    # 获得会话的sessionId
    sessionId = request.cookies.get('session')
    print(sessionId)
    return 'login success，sessionId={0}'.format(sessionId)

#删除session
@app.route('/delete/')
def delete():
    session.pop('username')
    return '删除会话成功'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)


# http://127.0.0.1/static/index.html