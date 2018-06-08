import urllib.request
import json
import os
response = urllib.request.urlopen("http://pvp.qq.com/web201605/js/herolist.json")
hero_json = json.loads(response.read())
hero_num = len(hero_json)
print(hero_json)
print("hero_num : " , str(hero_num))

# 文件夹不存在则创建
save_dir = 'D:\heroskin2\\'
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

for i in range(hero_num):
    # 获取英雄皮肤列表
    skin_names = hero_json[i]['skin_name'].split('|')
    #以|为标志将字符串分割开
    for cnt in range(len(skin_names)):
        save_file_name = save_dir + str(hero_json[i]['ename']) + '-' +hero_json[i]['cname']+ '-' +skin_names[cnt] + '.jpg'

        skin_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'+str(hero_json[i]['ename'])+ '/' +str(hero_json[i]['ename'])+'-bigskin-' + str(cnt+1) +'.jpg'
        if not os.path.exists(save_file_name):
            urllib.request.urlretrieve(skin_url, save_file_name)  #将远程数据下载到本地
            print('正在下载'+save_file_name )

