# -*- coding:utf-8 -*-
# 启动WSGI服务器，加载application()函数

# 从wsgiref模块导入
from wsgiref.simple_server import make_server
# 导入application函数
from hello import application

# 创建1个服务器，ip地址为空，端口是8000，处理函数是application
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')

# 开始监听HTTP请求
httpd.serve_forever()