# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__, static_url_path='', static_folder='')

@app.route('/user/<username>')
def sayHello(username):
    # 在页面中显示输入的姓名
    return '姓名是 %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 在页面中显示输入的邮编
    return '邮编是 %d' % post_id

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
