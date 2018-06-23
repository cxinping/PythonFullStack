from flask import render_template
from flask import Flask
from flask import request

app = Flask(__name__)

def valid_login(username, password):
    print('username=',username)
    print('password=',password)
    if username == 'abc' and password == '123':
        return True
    else:
        return False

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if valid_login(username,password):
            return render_template('result.html', username=username, password=password)
        else:
            error = '不合法的用户名和密码！！！'
    return render_template('login.html', error=error)

@app.route('/redirectLogin', methods=[ 'GET'])
def redirectLogin():
    return render_template('login.html' )

if __name__ == '__main__':
    app.run(debug=True)




