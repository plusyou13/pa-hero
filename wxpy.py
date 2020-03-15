# coding=utf-8
from __future__ import unicode_literals
from wxpy import *
import time
import requests
import  schedule
from threading import Timer
import urllib.request,json
bot = Bot(cache_path=True)
list=[ '李小畅']

def weather():
    url = 'https://free-api.heweather.com/v5/weather?city=CN101200101&key=5c043b56de9f4371b0c7f8bee8f5b75e'
    # 用urllib2创建一个请求并得到返回结果
    # req = urllib.request(url)
    resp = urllib.request.urlopen(url).read()
    # 将JSON转化为Python的数据结构
    json_data = json.loads(resp)
    return json_data

def get_news():
    """获取金山词霸每日一句，英文和翻译"""

    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    translation = r.json()['translation']
    print(content, note, translation)
    return content, note, translation


def send_news():
    try:
        w=weather()
        contents = get_news()
        # 你朋友的微信名称，不是备注，也不是微信帐号。
        for i in list:
            time.sleep(5)
            my_friend = bot.friends().search(i)[0]
            my_friend.send(contents[0])
            my_friend.send(contents[1])
            my_friend.send(contents[2])
            my_friend.send('pm2.5:'+w['HeWeather5'][0]['aqi']['city']['pm25'])
            my_friend.send('今天{0}: 气温：{1}°/{2}°'.format(str(w['HeWeather5'][0]['daily_forecast'][0]['date']),w['HeWeather5'][0]['daily_forecast'][0]['tmp']['min'],w['HeWeather5'][0]['daily_forecast'][0]['tmp']['max']))
            my_friend.send('穿衣建议：' + w['HeWeather5'][0]['suggestion']['drsg']['txt'])
            my_friend.send(u"早安 , have a good day!")


    except:
        # 你的微信名称，不是微信帐号。
        my_friend = bot.friends().search('7分钟')[0]
        my_friend.send(u"今天消息发送失败了")

if __name__ == "__main__":
    schedule.every().day.at("7:00").do(send_news)
    while True:
        schedule.run_pending()  # 确保schedule一直运行
        time.sleep(1)
    bot.join()  # 保证上述代码持续运行
