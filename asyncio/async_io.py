# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import asyncio
import time


async def taskIO_1():
    print('开始执行任务1...')
    await asyncio.sleep(2)  # 异步执行其他协程子任务，假设任务执行2s
    print('IO任务1已完成，耗时2s')
    return taskIO_1().__name__

async def taskIO_2():
    print('开始执行任务2...')
    await asyncio.sleep(3) # 假设任务执行3s
    print('IO任务2已完成，耗时3s')
    return taskIO_2().__name__

async def main():
    task = [taskIO_1(),taskIO_2()]  # 将任务打包
    done,pending = await asyncio.wait(task) # 异步执行打包任务
    for r in done:
        print('协程无序返回值：'+ r.result())

if __name__ == '__main__':
    start = time.time() # 开始时间
    loop = asyncio.get_event_loop() # 创建事件循环对象
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
    print('所有IO任务总耗时%.5f秒' % float(time.time()-start))