from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '123456':
        return render_template('sign-ok.html', username=username)
    return render_template('form.html', message='用户名或密码错误', username=username)

if __name__ == '__main__':
    app.run()
