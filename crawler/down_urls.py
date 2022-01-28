import os
import uuid
from urllib.request import urlretrieve
from tqdm import tqdm
os.system('pip3 install timeout-decorator')
import timeout_decorator
cur_path = os.path.abspath(os.path.dirname(__file__))


class Config():
    log_path = cur_path + "/download.log" # 爬取日志，以便从中获取urls
    save_path = cur_path + "/download/"  # 图片保存路径


def read_log(cfg):
    '''读取log的url'''
    file_list = open(cfg.log_path, "r").readlines()

    url_list = []
    for line in file_list:
        try:
            index = int(line.split(":")[0])  # 无异常则为图片
            url = line.replace(str(index) + ": ", "").strip()
            url_list.append(url)
        except:
            continue
    return url_list

@timeout_decorator.timeout(5) #耗时限制，单位为s
def down_img(url,save_path):
    urlretrieve(url,save_path)


def down_urls(url_list, save_path):
    '''
    根据url下载图片
    '''
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    for url in tqdm(url_list):
        try:
            down_img(url,save_path + str(uuid.uuid1()) + ".jpg")
        except:
            print("\n error url: ", url, "\n")


if __name__ == '__main__':
    cfg = Config()
    url_list = read_log(cfg)
    down_urls(url_list, cfg.save_path)
