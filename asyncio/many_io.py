# 普通代码（单线程）实现多个IO任务

import time # 导入时间模块
import asyncio # 导入异步io模块

@asyncio.coroutine # 表示协程的装饰器
def taskIO_1():
    print('开始运行IO任务1...')
    yield from asyncio.sleep(2) # asyncio.sleep(2)是另一个协程程序，假设该子任务执行2秒
    print('IO任务1已完成，耗时2s')
    return taskIO_1.__name__

@asyncio.coroutine # 表示协程的装饰器
def taskIO_2():
    print('开始运行IO任务2...')
    yield from asyncio.sleep(3) # 假设该子任务执行3s
    print('IO任务1已完成，耗时2s')
    return taskIO_2.__name__

@asyncio.coroutine
def main(): # 调用方
    task = [taskIO_1(), taskIO_2()] # 把所有任务添加到task列表中
    done, pending = yield from asyncio.wait(task) # 调用生成器，asyncio.wait：可等待对象的集合
    print(type(done))
    for r in done:
        print('协程任务返回值：'+r.result())

if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop() # 创建1个事件循环对象
    try:
        loop.run_until_complete(main()) # 完成事件循环知道最后一个任务结束
    finally:
        loop.close() # 结束所有事件循环
    print('所有IO任务总耗时%.5f秒' % float(time.time()-start ))

