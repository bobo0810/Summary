## 图片爬虫

## [AutoCrawler](https://github.com/YoongiKim/AutoCrawler) 

| 优点                                                         | 缺点                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1. 支持Google, Naver。<br/>2. 自动配置chrome驱动。<br/>3. 爬取数量无限制。 | 1. 图片下载经常超时。解决：外网服务器下载。<br/>2. Naver爬取的图片类型经常并非所需。 |

> 1. 仅Google可用。
> 2. 爬取时开启全局代理，且获取原图url。
> 3. 外网服务器根据url下载图片。  [down_urls.py](./down_urls.py)



## [Image-Downloader](https://github.com/sczhengyabin/Image-Downloader)

| 优点                                           | 缺点                                                         |
| ---------------------------------------------- | ------------------------------------------------------------ |
| 1. 支持Google,Baidu,Bing。<br/>2. 可视化界面。 | 1. 单搜索引擎爬取<br/>2. 手动配置chrome驱动，可能失败。<br/>3. 最多爬取2千张。 |

> 1. [下载驱动](https://chromedriver.chromium.org/downloads)后，放到项目根目录及bin目录即可。
>
> 2. Google不可用。



## Tricks

- 更多关键词：近义词、多场景称呼、英文等