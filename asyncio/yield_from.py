# -*- coding:utf-8 -*-

# 这个案例演示yield和yield from的区别

def generator_1(titles):
    yield titles

def generator_2(titiles):
    yield from titiles

titles = ['python', 'java', 'c++']
for title in generator_1(titles):
    print('生成器1：', title)

for title in generator_2(titles):
    print('生成器2：', title)