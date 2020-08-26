#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
import re
import base64
import bs4
from bs4 import BeautifulSoup
from time import *
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# user-agent
user = {
    'Host':'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding':'gzip, deflate,',
    'Connection':'keep-alive',
    'Cookie':'SESSIONID=DGKNigFU5xAqAv3fiy7TKS1pFnHK7e3t3xDZh71M7lX; JOID=V18dC09tSWn3rsT6YWCqudnw-zN9TGVK2Izl1kJPaEXUgebbTU2HIKWtyfVtBt9DKi8mXzaYTaXfPq9A2HKYdeY=; osd=VFsTBk5uTWf6r8f-b22rut3-9jJ-SGtH2Y_h2E9Oa0HajOfYSUOKIaapx_hsBdtNJy4lWziVTKbbMKJB23aWeOc=; _zap=cc6e25b7-6c2b-463f-9adc-a82460c2e7a5; _xsrf=0edad31c-7ee1-4c2f-87b9-1354661ba697; d_c0="AACR7U8yyhGPTgo8bTYT7TAoLaDaBrnFdBE=|1598406955"; KLBRSID=3d7feb8a094c905a519e532f6843365f|1598407080|1598406955; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1598406957; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1598406957; _ga=GA1.2.990646381.1598406958; _gid=GA1.2.1067406846.1598406958; capsion_ticket="2|1:0|10:1598406964|14:capsion_ticket|44:ZDFmODA3ZTA0NmIyNGUxNjg0NWVhM2MyN2M5ODZmODM=|cc579e584ee35d34b353d043193054d971f3554760c1090c6c50b75d2a76f40b"',
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

    for i in range(20):
        start_time = time()
        handle(url)
        sleep(1)
        # 防反爬，不能过快
        end_time = time()
        running_time = end_time - start_time
        print("running time:{:.4}s".format(running_time))