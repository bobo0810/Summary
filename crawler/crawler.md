## 图片爬虫

## [AutoCrawler](https://github.com/YoongiKim/AutoCrawler) 

| 优点                                                         | 缺点                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1. 支持Google, Naver。<br/>2. 自动配置chrome驱动。<br/>3. 爬取数量无限制。 | 1. 图片下载经常超时。解决：url需外网服务器下载。<br/>2. Naver爬取的图片类型经常并非所需。 |

Naver

- 需英文关键词 
- 观察是否符合需要

Google

- 爬取时开启全局代理，且获取原图url
- 外网服务器下载url

url外网下载

- 项目根路径下使用[down_urls.py](./down_urls.py)



## [Image-Downloader](https://github.com/sczhengyabin/Image-Downloader)

| 优点                                           | 缺点                                                         |
| ---------------------------------------------- | ------------------------------------------------------------ |
| 1. 支持Google,Baidu,Bing。<br/>2. 可视化界面。 | 1. 单搜索引擎爬取<br/>2. 手动配置chrome驱动，可能失败。<br/>3. 最多爬取2千张。 |

> [下载驱动](https://chromedriver.chromium.org/downloads)后，放到项目根目录及bin目录即可。

多搜索引擎爬取

- 项目根目录下使用[multi_keys_se.py](./multi_keys_se.py)



## Tricks

- 更多关键词：近义词、多场景称呼、英文等