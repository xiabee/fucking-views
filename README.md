# fucking-views

A script of increasing the views of website

一个简易的浏览量代刷脚本

#### 版本更新

* version：0.2
* time：2020.8.28 23:41
* 更新内容：新增**IP代理池**，减少被封IP的风险；由于`fake_useragent`不稳定，经常404，暂时下线ua池
* 取消代理：`view`函数中，将`res = requests.get(url, headers = user, proxies = proxies)`改为`res = requests.get(url, headers = user)`
* 稳定版多UA池和动态代理池正在开发中



#### 写在前面

* 单纯的遇到一些事情，想给某些问题送点流量，此脚本仅提供一点浏览量
* 目前仅使用单个UA，可能会被反爬机制制裁，多UA与多线程代刷正在开发中

#### 运行环境及依赖

* Python3
* requests
* bs4
* fake_useragent



#### 依赖安装方法

* 打开命令行，输入以下内容：

  ```
  pip3 install requests
  pip3 install bs4
  pip3 install fake_useragent
  ```
  


#### 程序使用方法

* 通过Python3运行`main.py`即可

```
  python3 main.py
```



#### 代刷地址修改

* 修改程序`if __name__ == "__main__":` 模块中的`url`
* 注意：本程序针对**知乎**网页，若修改为其他网站地址则需同时修改`handle`函数中的`content`的值



#### 程序不足

* 多UA，多IP，在写了，在写了
* 静态代理池通信不稳定，容易被封代理，延迟也比较高

#### 测试返回

  ```
Followers:1,052 Views:884,666   requesting time:0.984s  proxy:123.57.210.164:3128
Followers:1,052 Views:884,726   requesting time:1.11s   proxy:119.57.105.25:53281
Followers:1,052 Views:884,727   requesting time:1.264s  proxy:220.249.149.59:9999
Followers:1,052 Views:884,727   requesting time:1.161s  proxy:36.248.132.136:9999
Followers:1,052 Views:884,727   requesting time:0.958s  proxy:39.97.97.227:3128
Followers:1,052 Views:884,727   requesting time:1.192s  proxy:58.253.153.11:9999
Followers:1,052 Views:884,727   requesting time:1.007s  proxy:119.57.105.25:53281
Followers:1,052 Views:884,727   requesting time:0.8527s proxy:60.191.11.249:3128
Followers:1,052 Views:884,742   requesting time:1.408s  proxy:163.125.17.105:8888
  ```

