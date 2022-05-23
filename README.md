# EasyCampus

## 项目简介
这是一个基于Python的命令行连接**北理**校园网的小工具。

在我理的校园中，如果需要使用外网，是需要先登录认证后才可以使用外网。这一登录认证操作在图形化界面下易于完成。但在无任何界面的Linux/Unix系统下完成这一操作比较费力。

因此，需要一个可以在命令行下进行校园网登录认证的小工具。

目前，这个小工具已经实现了在Windows/Linux/Unix下的校园网认证与登出。

欢迎大家提建议~

## 使用说明
经过测试，该程序支持在Windows/CentOS/Ubuntu/macOS下使用。此外，程序也支持在Python2/3环境下使用（需要先装好 requests, argparse 包）。
- 配置模式
在该模式下，我们可以将自己的上网账号存储在配置文件中，免去每次登录、登出时手动输入密码的步骤。该模式适合在自己常用的电脑上使用。具体用法：
    1. 输入配置， `python easycampus.py -config -u 帐号 -p 密码`
    2. 登录， `python easycampus.py -login`
    3. 登出， `python easycampus.py -logout` 

- 直连模式
在该模式下，每次登录、登出，我们都需要手动输入自己的上网账号与密码。该模式适合在临时使用的电脑上使用。具体用法：
    1. 登录， `python easycampus.py -login -u 账号 -p 密码`
    2. 登出， `python easycampus.py -logout -u 账号 -p 密码`

- 定时模式
在该模式下，可以定时运行登录、登出命令，该模式适合在无人值守的机器上使用。具体用法 ：
    1. 搭配`配置模式`使用，在完成用户名、密码的配置后， `python easycampus.py -login -t 时间（以秒为单位）`
    2. 搭配`直连模式`使用，`python easycampus.py -login -u 账号 -p 密码 -t 时间（以秒为单位）`

## ToDo List
- [ ] 在线时长 查询功能
- [ ] 剩余流量 查询功能
- [ ] 余额 查询功能
- [ ] 当前IP 查询功能

