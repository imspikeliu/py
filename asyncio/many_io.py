# 普通代码（单线程）实现多个IO任务

import time
def taskIO_1():
    print('开始执行IO任务1...')
    time.sleep(2)   # 假设任务执行2s
    print('IO任务已完成，耗时2s')

def taskIO_2():
    print('开始执行IO任务2...')
    time.sleep(3)   # 假设任务执行3s
    print('IO任务已完成，耗时3s')

start = time.time()
taskIO_1()
taskIO_2()
end = time.time()

print('所有IO任务总耗时 %.5f' % float(end-start))



