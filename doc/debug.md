
## 尝试找到原本的连接是否有效

> 打开校园网页面，在左边填入账号信息，但不要点击登录
> 按F12打开开发者界面,选择Network栏
  
<img src="img/debug-1.jpg" style="border-radius:20px">
<br>
<br>

> 点击登录，抓包数据信息，在`header`中可以看到携带登录信息的URL,复制下来
  
<img src="img/debug-2.jpg" style="border-radius:20px">
<br>
<br>

> 粘贴到地址栏中访问，可以看到返回一段json如下图，代表测试成功了
  
<img src="img/debug-3.jpg" style="border-radius:20px">