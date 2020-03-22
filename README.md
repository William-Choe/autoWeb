## 环境配置
安装步骤：
1. 安装selenium: pip3 install selenium
2. 安装webdriver:
    Chrome: <http://chromedriver.storage.googleapis.com/index.html>
    Chromium: sudo apt-get install chromium-chromedriver
    Firefox: <https://github.com/mozilla/geckodriver/releases/>
    注：webdriver需要和对应的浏览器版本以及selenium版本对应。
3. webdriver安装路径
    Win: 复制webdriver到python安装目录下
    Linux/Mac: 复制webdriver到/usr/local/bin下

## 运行程序
```
# 直接运行
python3 autoWeb.py 学号 密码

# 脚本运行，支持填写多人信息
# 运行前需要更改：
# 1. 脚本log文件路径
# 2. 将程序参数改为自己的账户
bash run.sh
```

## 设置程序每天定时运行
```
crontab -e

# 在最后一行添加，每天凌晨十二点十分运行脚本
10 00 * * * /home/pi/autoWeb/autoWeb.sh

# 重启cron服务
service cron restart
```
