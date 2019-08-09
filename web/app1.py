# -*- coding:utf-8 -*-

# 从web框架导入模块
from flask import Flask, request, render_template

app = Flask(__name__) # 实例化1个app

# Flask通过装饰器在内部自动把URL和函数关联起来
# 首页
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', page_list=[1, 2, 3, 4, 5])
    
# 注册页面
@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')
    
# 注册功能
@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '1':
        return render_template('signin-ok.html', username=username)
    else:
        return render_template('form.html', message='用户名或密码错误!', username=username)
        
if __name__ == '__main__':
    app.run()
