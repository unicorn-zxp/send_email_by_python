# -*- coding = utf-8 -*-
# _author_ = 'Unicorn'
# time :2020/4/10 12:39
# 'keep calm and carry on'
# key注意替换

import requests
import json
import time

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
key=''  # 天行api网站上申请的密钥

class Crawl:

    def __init__(self, url):
        self.url = url

    def get_data(self):
        r = requests.get(self.url)
        content = json.loads(r.text)
        return content


def soup():  # 获取毒鸡汤的内容

    url = 'http://api.tianapi.com/txapi/dujitang/index?key=%s'%key
    s = Crawl(url)
    content = s.get_data()
    return content['newslist'][0]['content']


def constellation():  # 获取星座内容

    url1 = 'http://api.tianapi.com/txapi/star/index?key=%s&astro=taurus'%key
    url2 = 'http://api.tianapi.com/txapi/star/index?key=0%s&astro=leo'%key
    url3 = 'http://api.tianapi.com/txapi/star/index?key=%s'%key
    c1 = Crawl(url1)
    c2 = Crawl(url2)
    c3 = Crawl(url3)
    content1 = c1.get_data()
    content2 = c2.get_data()
    content3 = c3.get_data()

    if content1['code']==200:
        s = '<星座运势>：\n金牛座：\n幸运数字：%s   幸运颜色：%s\n今日概况：%s' % (content1['newslist'][6]['content'], content1['newslist'][5]['content'], content1['newslist'][8]['content'])
    else:
        s = '<星座运势>：\n金牛座：没有从互联网上获取到内容！'

    if content2['code']==200:
        v = '狮子座：\n幸运数字：%s   幸运颜色：%s\n今日概况：%s' % (content2['newslist'][6]['content'], content2['newslist'][5]['content'], content2['newslist'][8]['content'])
    else:
        v = '狮子座：\n没有从互联网上获取到内容'

    if content3['code'] == 200:
        w = '处女座：\n幸运数字：%s   幸运颜色：%s\n今日概况：%s' % (content3['newslist'][6]['content'], content3['newslist'][5]['content'], content3['newslist'][8]['content'])
    else:
        w = '处女座：\n没有从互联网上获取到内容'
    return [s, v, w]


def god_reply():  # 获取神回复

    url = 'http://api.tianapi.com/txapi/godreply/index?key=%s'%key
    g = Crawl(url)
    content = g.get_data()
    return [content['newslist'][0]['title'], content['newslist'][0]['content']]


def netease():  # 获取网易云热评

    url = 'http://api.tianapi.com/txapi/hotreview/index?key=%s'%key
    n = Crawl(url)
    content = n.get_data()
    return [content['newslist'][0]['content'],  '<'+content['newslist'][0]['source']+'>']


def one():  # 获取one的内容

    url = 'http://api.tianapi.com/txapi/one/index?key=%s'%key
    o = Crawl(url)
    content = o.get_data()
    return content['newslist'][0]['word']


def dog():

    url = 'http://api.tianapi.com/txapi/tiangou/index?key=%s'%key
    d = Crawl(url)
    content = d.get_data()
    return content['newslist'][0]['content']


def rainbow():

    url = 'http://api.tianapi.com/txapi/caihongpi/index?key=%s'%key
    ra = Crawl(url)
    content = ra.get_data()
    return content['newslist'][0]['content']


def taici():

    url = 'http://api.tianapi.com/txapi/dialogue/index?key=%s'%key
    t = Crawl(url)
    content = t.get_data()
    return [content['newslist'][0]['dialogue'],  '<'+content['newslist'][0]['source']+'>']


def weather():

    url = 'http://api.tianapi.com/txapi/tianqi/index?key=%s&city=合肥'%key
    w=Crawl(url)
    content =w.get_data()
    s = '今天是%s,天气：%s,最低气温：%s,最高气温：%s,实时温度为：%s,有%s,风力：%s\n张小培提醒你：%s\n'%(content['newslist'][0]['week'],
                                                                     content['newslist'][0]['weather'],
                                                                     content['newslist'][0]['lowest'],
                                                                     content['newslist'][0]['highest'],
                                                                     content['newslist'][0]['real'],
                                                                     content['newslist'][0]['wind'],
                                                                     content['newslist'][0]['windsc'],
                                                                     content['newslist'][0]['tips'])
    return s
