# -*- coding:utf-8 -*-

# 整数累计加和
# 子生成器、委托生成器、调用方

# 子生成器，完成具体求和任务
def gen_1():
    total = 0
    while True:
        x = yield
        print(x)
        if not x: # 如果x为None退出循环
            break
        total = total + x
    return total

# 委托生成器，负责调用子生成器
def gen_2():
    while True:
        total = yield from gen_1()
        print(total)

# 调用方
def main():
    g = gen_2()
    g.send(None) # 启动生成器
    g.send(2)
    g.send(3)
    g.send(None)


main()

print(not None)
