## 群晖Docker部署VSCode

### 部署vscode

[参考教程](https://zhuanlan.zhihu.com/p/380497442?utm_source=ZHShareTargetIDMore&utm_medium=social&utm_oi=959906746983174144)

### 外部访问

1. docker映射的端口避免8080

​		教程中`docker-compose.yml` 更改ports为*<u>8077</u>*:8080。此时docker内部访问地址为`127.0.0.1:8080`，docker外部的群晖访问地址为`群晖ip:8077`

2. 路由器端口映射



### 问题

1. 若Docker出现目录权限不足问题

   [方案1](https://wp.520810.xyz:666/?p=84)   [方案2](https://www.orcy.net.cn/1636.html)