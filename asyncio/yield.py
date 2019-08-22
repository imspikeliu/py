# !/usr/bin/env python3
# -*- coding:utf-8 -*-


def h():
    print('WenChuan')
    m = yield 5
    print(m)
    d = yield 12
    print('We are together!!!')

c = h()
x = c.send(None) # 启动生成器
y = c.send('Fighting!!!')

print('我们永远不会忘记：', x, '.', y)


