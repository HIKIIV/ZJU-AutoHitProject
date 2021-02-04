# ZJU-AutoHitProject
辅导员再也不用担心我忘记打卡了！

-----------------
这是一个针对ZJU每日健康上报的自动打卡小玩意儿，用了不能再水的selenium库。
本来是打算将它部署到树莓派上的，然而发现我的Raspbian系统是32位的，但chromedriver没有Linux下对应32位的版本...后来尝试用Firefox的geckodriver，又因神秘原因失败...最后只好部署在Windows下，设置成开机自动启动，这样只要我在某一天内打开了我的电脑，就不用怕这一天忘记打卡了qwq。

### 普通的食用说明：（巨佬们请忽略）
0. 需**正确安装python**(一切的前提)，Chrome浏览器(若使用其他浏览器需下载对应的驱动并在代码里做相应改动)
1. 安装selenium库。可以直接在命令行中输入`pip install selenium`
2. 安装chromedriver(具体见P.S.)
3. 下载上面的AutoHit.py
4. 把AutoHit.py里57行的Sno和Psw改成自己浙大统一身份认证的学号和密码（都是字符串）
5. 可以写一个批处理如
```bat
ping localhost -n 4
python D:\projects\Python\AutoHit.py
```
（里面应改成自己下载后AutoHit的位置）
并把它放到C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp目录下（在有的电脑上可能会有中文路径）

这样就可以高枕无忧啦~

**P.S.**chromedriver的安装：
  - 在Chrome设置->关于Chrome查到所使用的Chrome版本号
  - 在[这里](http://npm.taobao.org/mirrors/chromedriver/)下载对应版本的chromedriver
  - 将解压后的chromedriver.exe所在目录放到Path里
  - 在命令行里输入chromedriver看看是否正确安装
