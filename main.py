#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from time import *
from fake_useragent import UserAgent
ua = UserAgent()
# 使用 fake ua 以突破反爬机制
# ua.update()
# fake经常404，fake功能暂时关闭，后续fake正在开发

# user-agent
user = {
    'Host':'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding':'gzip, deflate,',
    'Connection':'keep-alive',
    
    'Upgrade-Insecure-Requests':'1',
    'Cache-Control':'max-age=0',
    'TE':'Trailers',
}

def view(url):
    try:
        res = requests.get(url, headers = user)
        status = res.status_code
        # print(status)
        if status != 200:
            print("Network Error:{}".format(status))
        else:
            return res
    except:
        print("URL ERROR!")

def handle(url):
    try:
        res = view(url)
        enc = res.encoding
        # print(enc)
        text = res.text.encode(enc)
        html = res.text
        
        soup = BeautifulSoup(html,'html.parser')
        [script.extract() for script in soup.findAll('script')]
        [style.extract() for style in soup.findAll('style')]
        # 去掉scrip和style
        
        content = soup.find_all(name='strong',attrs={"class":"NumberBoard-itemValue"},)
        num = []
        for con in content:
            x_num = con.get_text()
            num.append(x_num)
        print("Followers:{viewer}\tViews:{view}\t".format(viewer=num[0],view=num[1]), end='')
    except:
        pass

if __name__ == "__main__":
    url = 'https://www.zhihu.com/question/417174246'

    while(True):
        start_time = time()
        handle(url)
        sleep(1)
        # 防反爬，不能过快
        end_time = time()
        running_time = end_time - start_time
        print("running time:{:.4}s".format(running_time))