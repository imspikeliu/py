# -*- coding:utf-8 -*-

# 生产者-消费者协程模型
# 1、启动消费者生成器
# 2、生成东西，通过.send()传给yield，yield又返回值
# 3、生产者拿到消费者处理结果，继续生产
# 4、决定不生产了，通过c.close()关闭消费者，完成
# 消费者

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[消费者]正在消费%s...' % n)
        r = '200 ok'

def produce(c):
    c.send(None) # 启动消费
    n = 0
    while n < 5:
        n = n + 1
        print('[生产者]正在生产%s...' % n )
        r = c.send(n)
        print('[生产者]消费者返回:%s' % r)
    c.close()


c = consumer()
produce(c)