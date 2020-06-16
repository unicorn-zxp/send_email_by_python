# -*- coding = utf-8 -*-
# _author_ = 'Unicorn'
# time :2020/4/10 13:10
# 'keep calm and carry on'

#  用python批量发送邮件

from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import crawl_api_2 as ca
import time


def send_email(receiver, subject, content):
    sender = 'unicorn_zxp@163.com'
    smtpserver = 'smtp.163.com'

    username = 'unicorn_zxp@163.com'
    password = '' # 邮箱的授权密码

    msg = MIMEText(content, 'plain', 'utf-8')  # 中文需参数‘utf-8'，单字节字符不需要

    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = 'Unicorn<unicorn_zxp@163.com>'
    msg['To'] = receiver

    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    while 1:
        try:
            smtp.login(username, password)
            smtp.sendmail(sender, receiver, msg.as_string())
            break
        except:
            time.sleep(2)
            print('发送失败，正在重新尝试！')
            continue
    


def get_content():
    time_current = datetime.now().strftime('%Y-%m-%d')
    content_part = '今天是公元 %s ，张小培给您的播报内容如下：\n\n' % time_current
    weather_content=ca.weather()
    content_part = content_part + '<天气预报>：\n' + weather_content + '\n'
    soup_content = ca.soup()
    content_part = content_part + '<毒鸡汤>：\n'+soup_content + '\n\n'
    constellation_content = ca.constellation()
    content_part = content_part + constellation_content[0] + '\n\n'
    content_part = content_part + constellation_content[1] + '\n\n'
    content_part = content_part + constellation_content[2] + '\n\n'
    dog_content = ca.dog()
    content_part = content_part + '<舔狗日记>：\n' + dog_content + '\n\n'
    rainbow_content = ca.rainbow()
    content_part = content_part + '<彩虹屁>：\n' + rainbow_content + '\n\n'  
    #reply_content = ca.god_reply()
    #content_part = content_part + '<神回复>:\n问：' + reply_content[0] + '\n答：' + reply_content[1] + '\n\n'
    net_content = ca.netease()
    content_part = content_part + '<网易云热评>：\n' + net_content[0] + '\n来源：' + net_content[1] + '\n\n'
    one_content = ca.one()
    content_part = content_part + '<one每日精选>：\n' + one_content + '\n\n'
    taici_content=ca.taici()
    content_part = content_part + '<经典台词>：\n' + taici_content[0] + '\n来源：' + taici_content[1] + '\n\n'

    content_part += '以上内容完全来源于互联网，张小培不负任何责任！！！\n\n今天的每日播报到这里就结束了，感谢您的阅读，我们明天再见！\n\n退订回复TD！'
    return content_part


if __name__ == '__main__':
    receivers = ['279035162@qq.com']
    subjects = '张小培今日份播报'
    contents = get_content()
    print('内容获取完毕')
    for re in receivers:
        send_email(re, subjects, contents)
        print('邮件发送成功')
