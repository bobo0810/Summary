[TOC]



## 群晖设置导航页

[参考](https://post.smzdm.com/p/adwlg5rn/)



## 群晖Docker部署gogs

gogs：轻量级git服务器

1. 安装gogs

![](imgs/image-20211231162800626.png)



<img src="imgs/WechatIMG1468.png" style="zoom:80%;" />

<img src="imgs/WechatIMG1488.png" >

<img src="imgs/WechatIMG1471.png" >

<img src="imgs/WechatIMG1472.png" >

配置后启动容器

<img src="imgs/WechatIMG1474.png" >

2. 初始化gogs配置

   设置参数后，点击**立即安装**

   访问安装地址 **群晖内网地址:http端口号**   eg: **192.168.3.8:3334**

   > 假设群晖有动态公网ip，绑定的外网可访问域名为**hahaha.familyds.com**

   <img src="imgs/WechatIMG1477.png" >



<img src="imgs/WechatIMG1479.png" >

3. 外网访问

​	路由器放开http端口后，外网即可通过**http://hahaha.familyds.com:3334/**访问

   <img src="imgs/WechatIMG1481.png" >

<img src="imgs/WechatIMG1484.png" >





3. 外网测试

添加ssh公钥

> 查看命令  cat ~/.ssh/id_rsa.pub

<img src="imgs/WechatIMG1485.png" >

新建库并推送

<img src="imgs/WechatIMG1486.png" >



参考

[Docker-Ubuntu-Gogs部署及配置时遇到的问题](https://www.itfanr.cc/2017/03/24/docker-ubuntu-gogs-problems/)

[gogs官方库](https://github.com/gogs/gogs)

[群晖docker安装gogs及mysql进行代码管理](https://blog.csdn.net/hahofe/article/details/119106256)



