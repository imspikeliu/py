# -*- coding:utf-8 -*-

from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)' % (name,os.getpid()))
    

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid() )
    # 实例化子进程,target:执行的目标函数，args:函数传入的参数，数据类型为元祖
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    # 开始执行子进程
    p.start()
    # 等子进程结束后再继续执行
    p.join()
    print('Child process end.')