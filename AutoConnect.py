#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Author__ = "YINGHAI"
__Email__ = "pyj2897022134@gmail.com"

import socket,sys,requests
from plyer import notification
import win32api, win32gui


class AutoConnect:
    def __init__(self,loginIp=None,user_account=None,user_password=None):
        self.ip = self.get_ip()
        self.user = user_account
        self.password = user_password
        self.loginIP = loginIp

    def outputArgv(self):
        '''
        测试参数接收
        :return:
        '''
        print(self.loginIP,self.user,self.password,self.ip)
        return None
    def get_ip(self):
        '''
        获取ip地址
        :return:
        '''
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('3.3.3.3', 80))
        ip = s.getsockname()
        s.close()
        return ip[0]
    def Login(self):
        '''
        自动化登录流程
        目前已完成使用GET登陆的流程
        TODO POST登录流程 
        :return:
        '''
        URL = f"http://{self.loginIP}:801/eportal/?c=Portal&a=login&callback=dr1003&login_method=1&user_account={self.user}&user_password={self.password}&wlan_user_ip={self.ip}&wlan_user_ipv6=&wlan_user_mac=000000000000"
        #print(URL)
        res = requests.get(URL)
        massage ="""
        """
        if '"msg":""' in res.text:
            print('当前设备已登录')
            message = "当前设备已登录"
            
        elif r'\u8ba4\u8bc1\u6210\u529f' in res.text:
            print('登录成功')
            message = "登录成功"
        elif 'bGRhcCBhdXRoIGVycm9y' in res.text:
            print("密码错误")
            message = "密码错误"
        elif r'\u8d26\u53f7\u4e0d\u80fd\u4e3a\u7a7a' in res.text:
            print("账号不能为空")
            message = "账号不能为空"
        elif 'aW51c2UsIGxvZ2luIGFnYWluL' in res.text:
            self.Login()
        else:
            print("您可能欠费停机")
            message = "您可能欠费停机"
        
        notification.notify(
            title="校园网连接",
            #app_name= "SNAC",
            message = message,
            app_icon="",
            timeout=5
        )
        return None


ct = win32api.GetConsoleTitle()
hd = win32gui.FindWindow(0,ct)
win32gui.ShowWindow(hd,0)

login_ip = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]

a =AutoConnect(login_ip,user,password)
a.Login()