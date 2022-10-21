@echo off

if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit
:begin
REM

python AutoConnect.py脚本绝对路径 校园网网址 登录用户名 密码
