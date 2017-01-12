from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/sign', methods=['GET'])
def sign_form():
    return '''<form action="/sign" method="post">
                <p><input type="text" name="username"></p>
                <p><input type="password" name="password"></p>
                <p><button type="submit">登录</button></p>
            </form>'''

@app.route('/sign', methods=['POST'])
def signin():
    #需要从表单读取内容
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h1>欢迎来到圣承方略!!!</h1>'
    else:
        return '<h1>您输入的用户名或密码有误</h1>'

if __name__ == '__main__':
    app.run()