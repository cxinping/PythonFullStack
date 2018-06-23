from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World! bbbb'

if __name__ == '__main__':
    app.debug = True
    app.run()

