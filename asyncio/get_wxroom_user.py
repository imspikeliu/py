# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 获取群成员的信息

import itchat, datetime
from itchat.content import TEXT


class WeChat(object):
    def get_all_info_from_wechat(self):
        itchat.auto_login(enableCmdQR = False)
        # 获取群
        roomslist = itchat.get_chatrooms()
        # 群名称
        itchat.dump_login_status()  # 显示所有的群聊信息，默认是返回保存到通讯录中的群聊
        myroom = itchat.search_chatrooms(name=u'小马飞单市场伙伴群')  # 群聊名称
        gsq = itchat.update_chatroom(myroom[0]['UserName'], detailedMember=True)

        l = gsq['MemberList']
        for i in l:
            print('昵称:%s 签名：%s 性别：%s ' % (i['NickName'],i['Signature'],i['Sex']))



if __name__ == '__main__':
    obj = WeChat()
    data = obj.get_all_info_from_wechat()

