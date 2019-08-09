# -*- coding:utf-8 -*-

# 整数累计加和
# 子生成器、委托生成器、调用方

# 子生成器，用于计算总和并返回
def generator_1():
    total = 0
    while True:
        x = yield
        print('加',x)
        if not x:
            break
        total = total + x
    return total


# 委托生成器，用于委托子生成器完成任务
def generator_2():
    while True:
        total = yield from generator_1()
        print('加的总和是：', total)

# 调用方
def main():
    g2 = generator_2()
    g2.send(None)
    g2.send(2)
    g2.send(3)
    g2.send(None)

main()
