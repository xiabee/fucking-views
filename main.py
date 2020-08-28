#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from time import *
import random
from fake_useragent import UserAgent

ua = UserAgent()

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
proxies = {
    'http': '36.248.129.84:9999',
    'https': '36.248.129.84:9999'
}



def view(url):
    try:
        res = requests.get(url, headers = user, proxies = proxies)
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
        # 寻找流量次数
        
        num = []
        for con in content:
            x_num = con.get_text()
            num.append(x_num)
        print("Followers:{viewer}\tViews:{view}\t".format(viewer=num[0],view=num[1]), end='')
    except:
        return 0

if __name__ == "__main__":
    url = 'https://www.zhihu.com/question/417174246'

    file = './proxy.txt'
    f = open(file,mode='r',encoding='utf-8')
    proxy = []
    for line in f:
        line=line.strip('\n')
        proxy.append(line)
    # 代理池

    while(True):
        # user['User-Agent'] = ua.random
        # ua池

        tmp_proxy = proxy[random.randint(0,len(proxy)-1)]
        proxies ={
            'http':tmp_proxy,
            'https':tmp_proxy,
        }
        # 代理池

        start_time = time()
        flag = handle(url)
        # 记录是否爬取成功

        a = random.uniform(0.1,0.5)
        sleep(0.5)
        sleep(a)
        # 防反爬，生成随机时间间隔
        end_time = time()
        running_time = end_time - start_time
        if flag!=0:
            print("requesting time:{:.4}s\tproxy:{}".format(running_time,tmp_proxy))