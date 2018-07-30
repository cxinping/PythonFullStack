# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'

if __name__ == '__main__':
    app.run()
