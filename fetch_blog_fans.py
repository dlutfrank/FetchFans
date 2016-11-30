import requests
from bs4 import BeautifulSoup
import utils

TAG = 'blog_fans'

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'
}


def log(msg):
    utils.log(utils.log_level_debug, TAG, msg)


def weibo_fans(url):
    result = {

    }
    if not url:
        return result
    log(url)
    try:
        resp = requests.get(url, headers=header, timeout=10)
        log(resp.status_code)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, 'lxml')
            fans = soup.select('#comp_901_attention > strong')
            if fans:
                log(fans[0].get_text())
                result = {
                    'url': url,
                    'fans': fans[0].get_text()
                }
    except Exception as ex:
        log(ex)

    return result
