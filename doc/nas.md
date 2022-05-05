### 常见问题

1. 群晖DDNS`不生效`或`过期`

   （1）控制面板->安全性->证书，删掉该域名证书

   （2）外部访问->DDNS，再次申请该域名即可。

2. 访问权限不足

   [方案1](https://wp.520810.xyz:666/?p=84)   [方案2](https://www.orcy.net.cn/1636.html)

3. USB转2.5G网口

   [参考1 ](https://post.smzdm.com/p/amxqo29p/)  [参考2](https://post.smzdm.com/p/aoxq39q9/)

4. Docker权限

   PUID=1026, PGID=100

5. 群晖无法下载Docker镜像

​	   [手动下载导入](https://github.com/NotGlop/docker-drag)

6. “系统内存即将用尽” or  [xxx] stopped running because the system is out of memory.

   可能原因：docker镜像占用内存过大

   解决方案：加入内存限制



### 技巧

1. 自动更新Docker镜像

```bash
sudo docker run -d \    
     --name watchtower_dev \    
     --restart=always \    
     -e TZ=Asia/Shanghai \    
     -v /var/run/docker.sock:/var/run/docker.sock \    
     containrrr/watchtower:latest-dev --cleanup --interval 1200
```

