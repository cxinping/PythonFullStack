# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test():
    ls =[1,2,3,4]
    return str(ls)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)

# http://127.0.0.1