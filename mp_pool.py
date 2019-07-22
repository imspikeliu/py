# -*- coding:utf-8 -*-

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    # 开始时间，时间戳
    start = time.time()
    # 间隔时长
    time.sleep(random.random() * 3)
    # 结束时间
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))
    
if __name__ == '__main__':
    # 打印父进程id
    print('Parent process %s.' % os.getpid())
    # 实例化进程池
    p = Pool(4)
    # 循环进程池，每个进程执行一个任务
    for i in range(5):
        # long_time_task:要执行的函数，args:函数参数
        p.apply_async(long_time_task, args = (i,))
    print('Waiting for all subprocesses done...')
    # 调用p.join()之前必须调用p.close()，调用p.close()之后就不能再添加新的process了
    p.close()
    # 等子进程结束后再继续执行
    p.join()
    print('All subprocesses done')