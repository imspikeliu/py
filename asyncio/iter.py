# -*- coding:utf-8 -*-
from collections.abc import Iterable
from collections.abc import Iterator

# 生成器函数，含yield关键词
def gen():
    sum = 0
    r = yield sum
    sum = sum + r
    print('sum的值为：%s' % sum)
    r = yield sum
    sum = sum + r
    print('sum的值为：%s' % sum)
    r = yield sum

# 创建生成器
c = gen()
print(type(c)) # 生成器

# 启动生成器
a = c.send(None)
print('生成器返回的值为：%s' % a)
a = c.send(1)
print('生成器返回的值为：%s' % a)
a = c.send(1)
print('生成器返回的值为：%s' % a)

c = (x * x for x in range(10))
for x in c:
    print(x)


