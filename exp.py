#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from ua import *
import chardet
url = 'https://www.zhihu.com/question/417174246'

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

def test(url):
    try:
        res = view(url)
        enc = res.encoding
        # print(enc)
        text = res.text.encode(enc)
        html = res.content


        soup = BeautifulSoup(html,'html.parser')
        [script.extract() for script in soup.findAll('script')]
        [style.extract() for style in soup.findAll('style')]
        # 去掉scrip和style
        content = soup.find_all(name='div',attrs={"class":"NumberBoard-itemName"},)
        print(soup)
    except:
        pass
if __name__ == "__main__":  
    test(url)