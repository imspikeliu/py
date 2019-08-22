# -*- coding:utf-8 -*-

# 这个案例演示yield和yield from的区别

def gen_1(title):
    yield title

def gen_2(title):
    yield from title

title = ['php', 'python', 'java']

for x in gen_1(title):
    print(x)

for x in gen_2(title):
    print(x)


b = b'aaa'
print(type(b))

print(b'aaa'.decode())

str = 'aaa'
print(str.encode('utf-8'))