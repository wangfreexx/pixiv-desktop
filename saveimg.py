#-*- coding:utf-8 -*-

import requests
import re
import os

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'

headers1 = ({
    'Referer': 'http://www.pixiv.net/',
    'User-Agent': user_agent
})


def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:  # 如果不存在则创建目录
        print ('Establish'+str(path) + 'Succes' ) # 创建目录操作函数
        os.makedirs(path)
        return True
    else:  # 如果目录存在则不创建，并提示目录已存在
        print (str(path) + 'Already exist')
        return False


def save(dataid, cookies):
    b=0
    dataidurl = 'http://www.pixiv.net/member_illust.php?mode=medium&illust_id=' + str(dataid)
    res1 = requests.get(url=dataidurl, cookies=cookies,
                        headers=headers1)  # 相应id网站
    content1 = res1.text
    pattern1 = re.compile('(?<= data-src=")\S*(?=" class="original-image">)')
    originaltus = re.findall(pattern1, content1)
    if not originaltus:
        dataidurl = 'http://www.pixiv.net/member_illust.php?mode=manga&illust_id=' + str(dataid)
        res2 = requests.get(url=dataidurl, cookies=cookies,
                        headers=headers1)
        content2 = res2.text
        pattern2 = re.compile('(?<=data-filter="manga-image" data-src=")\S*(?=" data-index)')
        originaltus= re.findall(pattern2, content2)
        if not originaltus:
            print (str(dataid) + 'id'+'not found')
            return 4

    for originaltu in originaltus:
        content3 = originaltu
        pattern3 = re.compile('png')
        ifpng = re.findall(pattern3, content3)
        if not ifpng:
                str1 = 'jpg'
        else:
                str1 = 'png'  # 判断后缀是jpg还是png
        print (str(dataid) +'-'+str(b)+ ' Downing')
        pic = requests.get(originaltu, stream=True,
                               cookies=cookies, headers=headers1)
        string = 'pixiv' + str(dataid) + '-' + 'p' + str(b) + '.' + str1
        fp = open(string, 'wb')
        fp.write(pic.content)
        fp.close()  # 保存图片
        print (str(dataid)+'-'+str(b) + 'Down Succes')
        b=b+1
        return 0
