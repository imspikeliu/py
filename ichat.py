# - * - coding:utf-8 - * - 定义代码的编码格式，Python代码都需要申明
# 首先，导入相关的功能模块
import itchat  # 导入封装好的微信模块
import datetime  # 导入时间模块，用于处理时间
import time  # 导入时间模块，用于处理时间，这两个模块都是处理时间，只是功能有差异

# 然后生成二维码，登录微信，找到指定的好友
itchat.auto_login(hotReload=True)  # 登录微信，hotReload=True是避免每次都扫码登录
user = itchat.search_friends(name=u'Xu')  # 找到发送消息的好友，昵称即可
userName = user[0]['UserName']  # user是个列表，从列表中获取用户名

# 最后，写个循环，在指定时间给好友发送消息
while 1:  # 无限循环
    now = datetime.datetime.now()  # 获取当前时间datetime.datetime(2019, 6, 13, 15, 7, 30, 443310)
    now_str = now.strftime('%Y/%m/%d %H:%M:%S')[11:]  # 格式化时间并截取11位后面的时间(2019/06/13 15:11:53)
    print('\r{}'.format(now_str), end='')  # 显示时间，使用format格式化函数
if now_str in ['15:46:00']:
        itchat.send('Hi，妹子，下午好！久坐伤身哦，去接杯水，顺便走动走动吧！', toUserName=userName)
if now_str in ['17:00:00']:
        itchat.send('快要下班啦，工作做完了吗？做完了就看点资料学习下吧，放松放松！', toUserName=userName)
    time.sleep(1)  # 推迟调用线程运行

if __name__ == '__main__':  # 文件作为脚本直接执行时执行以下方法，被其他模块导入不执行
    itchat.auto_login()
    itchat.run()