import requests
import re
import utils

TAG = 'sina_fans'

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'SINAGLOBAL=5972055251988.291.1473232937086; SUB=_2AkMvTAjBQ8NhrAFWmPwUzG3iaI5H-jydeF23An7uJhMyPxh77msvqSU5KY6BCx8dddINkGqIb3MthedqHw..; SUBP=0033WrSXqPxfM72QWs9jqgMF55529P9D9W5qmlSmYXkUgTdbPuJ4SMhV5JpX5KzhUgL.FozNehBpehq7She2dJLoI7L.dGHX9riydJjt; SUHB=0u5Alm3IXT3Glk; _T_WM=cce841e61dc43e12f23921a31fce34ce; _s_tentry=zihaolucky.github.io; Apache=7525194746974.928.1480056269254; ULV=1480056270100:11:2:1:7525194746974.928.1480056269254:1478347594465; YF-V5-G0=a0e87040bfaca9b1b05c465a9e888d2d; YF-Ugrow-G0=3a02f95fa8b3c9dc73c74bc9f2ca4fc6; YF-Page-G0=046bedba5b296357210631460a5bf1d2; TC-V5-G0=05e7a45f4d2b9f5b065c2bea790496e2; TC-Ugrow-G0=0149286e34b004ccf8a0b99657f15013; UOR=zhangge.net,widget.weibo.com,cuiqingcai.com; TC-Page-G0=e2379342ceb6c9c8726a496a5565689e; login_sid_t=c1b57e04d2b5dc995823cc9758ea0844; WBtopGlobal_register_version=5b56985b93d98642',
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
