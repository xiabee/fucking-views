# fucking-views

A script of increasing the views of website

一个简易的浏览量代刷脚本

#### 写在前面

* 单纯的遇到一些事情，想给某些问题送点流量，此脚本仅提供一点浏览量
* 目前仅使用单个UA，可能会被反爬机制制裁，多UA与多线程代刷正在开发中

#### 运行环境及依赖

* Python3
* requests
* bs4



#### 依赖安装方法

* 打开命令行，输入以下内容：

  ```
  pip3 install requests
  pip3 install bs4
  ```

  

#### 程序使用方法

* 通过Python3运行`main.py`即可

  ```
  python3 main.py
  ```



#### 代刷地址修改

* 修改程序第59行`if __name__ == "__main__":` 模块中的`url`
* 注意：本程序针对**知乎**网页，若修改为其他网站地址则需同时修改第49行`content`的值



#### 程序不足

* 使用默认回显，在网站请求速度过慢时程序终端无回显......
* 第61行的`for`循环可以直接改成`while(True)`

#### 测试返回

```
Followers:508   Views:318,230   running time:1.559s
Followers:508   Views:318,230   running time:1.549s
Followers:508   Views:318,230   running time:1.225s
Followers:508   Views:318,230   running time:1.264s
Followers:508   Views:318,230   running time:1.382s
Followers:508   Views:318,230   running time:1.207s
Followers:508   Views:318,230   running time:1.656s
Followers:508   Views:318,230   running time:1.242s
Followers:508   Views:318,291   running time:1.557s
Followers:508   Views:318,291   running time:1.287s
```



