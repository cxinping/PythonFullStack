from flask import Flask
from flask import request       # 接收数据

app = Flask(__name__, static_url_path='', static_folder='')

@ app.route('/register_get', methods=['GET' ])
def register_get():
    print("返回请求类型=", request.method)

    if request.method == "GET":
        username = request.args.get('username')
        password = request.args.get('password')  # 返回index中输入的password
        password2 = request.args['password2']
        print("username={0},password={1},password2={2}".format(username , password, password2))

        # 输入密码要和确认密码一样，输入密码要大于等于3
        if password and len(password) >= 3 and password == password2:
            print('注册成功')
        else:
            print('失败')
            return '注册失败，输入密码要和确认密码一样，输入密码要大于等于3'

        # 姓名长度不能小于3
        if len(username) < 3:
            print('注册失败,注册用户名长度不能小于3')
            return '注册失败,注册用户名长度不能小于3'
        else:
            print('注册成功')
    return '注册成功'

@app.route('/register_post', methods=['POST'])
def register_post():
    username = request.form.get('username')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    print("username={0},password={1},password2={2}".format(username , password, password2))

    return 'ok'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
