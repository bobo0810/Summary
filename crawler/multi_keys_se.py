import os
import itertools
cur_path=os.path.abspath(os.path.dirname(__file__))

class Config():

    #================================================
    keywords=['猫','狗','pet cat','cat','dog']
    subject="animal"
    engines = ["Google"]  # 支持多搜索引擎 "Google"(需全局代理), "Bing","Baidu"  
    # ================================================


    max_number=2000 # 单keyword 单engines的最大下载数,最多2千
    output=cur_path+"/download_images_"+subject #图片保存路径
    logs=cur_path+"/logs_"+subject #爬取日志
    timeout=10 #下载单张图片的超时限制


def main(cfg):
    print("save imgs in %s,log in %s  "%(cfg.output,cfg.logs))
    if not os.path.exists(cfg.logs):
        os.makedirs(cfg.logs)


    engine_keyword_list=list(itertools.product(cfg.engines, cfg.keywords))
    for engine,keyword in engine_keyword_list:
        save_path=cfg.output+"/"+engine+"_"+keyword.replace(" ","_")
        log_path=cfg.logs+"/"+engine+"_"+keyword.replace(" ","_")+".log"
        keyword=keyword.replace(" ","\ ") # “\”表明后续字符为原意,而非命令 　　
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        # 后台下载
        os.system("nohup python -u  image_downloader.py --timeout %d --engine %s   --driver chrome_headless --max-number  %d --output %s  %s  > %s 2>&1 &  "%(cfg.timeout,engine,cfg.max_number,save_path,keyword,log_path))

if __name__ == '__main__':
    cfg=Config()
    main(cfg)