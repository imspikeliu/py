# -*- coding:utf-8 -*-

import asyncio

@asyncio.coroutine
def hello():
    print('hello,world!')
    # 异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(5)
    print('hello,world!')

# 获取Eventloop
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()