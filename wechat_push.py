# - * - coding:utf-8 - * - 定义代码的编码格式，Python代码都需要申明
# 首先，导入相关的功能模块
import itchat       # 导入封装好的微信模块
import datetime     # 导入时间模块，用于处理时间
import time         # 导入时间模块，用于处理时间
import pymysql

# 打开数据库
db = pymysql.connect(
    '39.106.144.205',
    'root',
    'cainiao360.com',
    'cainiao360'
)

# cursor()方法操作游标
cursor = db.cursor()





# 生成二维码，登录微信，找到指定的好友
itchat.auto_login(hotReload=True)  # 登录微信，hotReload=True是避免每次都扫码登录
chatrooms = itchat.search_chatrooms(name=u'菜鸟抢单管理群')  # 找到微信群
userName = chatrooms[0]['UserName']  # 从列表中获取用户名


while True:
    now = datetime.datetime.now()  # 获取当前时间datetime.datetime(2019, 6, 13, 15, 7, 30, 443310)
    now_str = now.strftime('%Y/%m/%d %H:%M:%S')[11:]  # 格式化时间并截取11位后面的时间(2019/06/13 15:11:53)
    print('\r{}'.format(now_str), end='')  # 显示时间，使用format格式化函数

    if now_str in ['17:09:00']:

        '''当日数据'''
        # 使用execute方法执行sql语句
        cursor.execute('''
        SELECT
        	sum(user_money) as sum_money
        FROM
        	fd_account_log 
        WHERE
        	change_type IN ( 5,100 )
        	and DATE_FORMAT( FROM_UNIXTIME(change_time), '%Y%m%d' ) = DATE_FORMAT( CURDATE( ) , '%Y%m%d' )

        ''')

        # 使用fetchone()获取单条数据
        day = int(cursor.fetchone()[0])

        '''当月数据'''
        # 使用execute方法执行sql语句
        cursor.execute('''
        SELECT
        	sum(user_money) as sum_money
        FROM
        	fd_account_log 
        WHERE
        	change_type IN ( 5,100 )
        	and DATE_FORMAT( FROM_UNIXTIME(change_time), '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )

        ''')

        # 使用fetchone()获取单条数据
        data = int(cursor.fetchone()[0])

        itchat.send('【菜鸟数据】今日累计充值：%d元，当月累计充值金额：%d元，当月充值目标200,000' % (day,data), toUserName=userName)

    time.sleep(1)  # 推迟1秒执行

if __name__ == '__main__':  # 被其他模块导入不执行
    itchat.auto_login()
    itchat.run()