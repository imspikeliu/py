# -*- coding:utf-8 -*-

from flask import Flask # Web框架
from flask import request 

app = Flask(__name__) # 实例化1个app

# Flask通过装饰器在内部自动把URL和函数关联起来
@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

# 登录表单
@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

# 登录
@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin! </h3>'
    else:
        return '<h3> Bad username or password</h3>'

if __name__ == '__main__':
    app.run()