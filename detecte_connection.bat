:check
cls
ping -n 4 www.baidu.com
IF ERRORLEVEL 1 goto :connection
IF ERRORLEVEL 0 goto :check

:connection
echo "开始连接"
python 脚本绝对路径/AutoConnect.py 校园网网址 登录用户名 密码
goto :check