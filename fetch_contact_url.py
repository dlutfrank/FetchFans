import requests
from bs4 import BeautifulSoup
import re
import utils
import time

TAG = 'contact'


def log(msg):
    utils.log(utils.log_level_debug, TAG, msg)


header = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
    "Accept-Encoding": "identity",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
}

url_prefix = "http://www.zhongchou.com"


def contact_info(url_path):
    info_url = {
        'home_page': url_path
    }
    if (not url_path) or (url_path == 'null'):
        return info_url

    log(url_path)
    try:
        resp = requests.get(url_prefix + url_path, headers=header, timeout=20)
        log(resp.status_code)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, 'lxml')
            # uid = soup.find(text=re.compile("UID = \'([a-z0-9]{24})\'"))
            # real = re.findall('\'([a-z0-9]{24})\'', uid)
            uid = re.findall("UID = \'([a-z0-9]{24})\'", soup.text)
            if uid:
                info_url['uid'] = str(uid[0])
                time.sleep(5)
                return fetch_info(info_url)
    except Exception as ex:
        log(ex)
    return info_url


info_prefix = 'http://www.zhongchou.com/prpc/userInfo,home-userinfo-v-3-user_id-'


def fetch_info(info_url):
    info = info_url
    if (not info_url) or (not info_url.get('uid')):
        return info
    try:
        url = info_prefix + str(info_url['uid'])
        resp = requests.get(url, headers=header, timeout=10)
        if resp.status_code == 200:
            soup = resp.json()
            info['sina_url'] = soup['userInfo']['sina_url']
            info['blog_url'] = soup['userInfo']['blog_url']
    except Exception as ex:
        print(ex)
    return info
