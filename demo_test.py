import requests
import utils
import re

TAG = 'blog_fans'

url = 'http://weibo.com/u/1800407450'

cookie = '##'

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': cookie,
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'
}


def log(msg):
    utils.log(utils.log_level_debug, TAG, msg)


def sina_fans(url):
    result = {

    }
    if not url:
        return result
    log(url)
    try:
        resp = requests.get(url, headers=header, timeout=10)
        log(resp.status_code)
        if resp.status_code == 200:
            page = resp.content.decode('utf-8')
            fans = re.findall(r'W_f18\\\">(\d+)<\\/strong><span class=\\\"S_txt2\\\">粉丝', page)
            log(fans)
            if fans:
                result = {
                    'url': url,
                    'fans': str(fans[0])
                }
    except Exception as ex:
        log(ex)
    return result


if __name__ == '__main__':
    sina_fans(url)
