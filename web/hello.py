# -*- coding:utf-8 -*-

# hello.py WSGI处理函数

# 定义函数，处理请求，environ：包含所有http请求的dict，start_response：发送http响应的函数
def application(environ, start_response):
    start_response('200 ok', [('Content-Type', 'text/html')])
    body = '<h1>hello, %s</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]