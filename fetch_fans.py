from threading import Thread
import time
import queue
import utils

import fetch_contact_url
import fetch_sina_fans
import fetch_blog_fans

TAG = 'contact'


def log(msg):
    utils.log(utils.log_level_debug, TAG, msg)


q = queue.Queue(100)

start = True

sep = '||'


class ProducerThread(Thread):
    def run(self):
        global q
        global start
        while start:
            with open(r'uhp.txt') as datafile:
                for line in datafile:
                    contact = fetch_contact_url.contact_info(line.strip('\n'))
                    q.put(contact)
                    time.sleep(5)
            start = False


class ConsumerThread(Thread):
    def run(self):
        global q
        global start
        fo = open(r'fans.txt', 'w+')
        while start or (not q.empty()):
            contact = q.get()
            if contact:
                if contact.get('sina_url'):
                    fans = fetch_sina_fans.sina_fans(contact['sina_url'])
                    if fans:
                        contact['sina_fans'] = fans.get('fans')
                    else:
                        contact['sina_fans'] = 'null'
                if contact.get('blog_url'):
                    fans = fetch_blog_fans.weibo_fans(contact['blog_url'])
                    if fans:
                        contact['blog_fans'] = fans.get('fans')
                    else:
                        contact['blog_fans'] = 'null'
            fo.write(ps(contact))
            fo.flush()
            q.task_done()
            time.sleep(5)
        fo.close()


def ps(info):
    result = ''
    if info:
        if info.get('home_page'):
            result += str(info['home_page'])
        else:
            result += 'null'

        result += sep

        if info.get('sina_url'):
            result += str(info['sina_url'])
        else:
            result += 'null'

        result += sep

        if info.get('sina_fans'):
            result += str(info['sina_fans'])
        else:
            result += 'null'

        result += sep

        if info.get('blog_url'):
            result += str(info['blog_url'])
        else:
            result += 'null'

        result += sep

        if info.get('blog_fans'):
            result += str(info['blog_fans'])
        else:
            result += 'null'

        result += '\n'

    else:
        result = 'null' + sep + 'null' + sep + 'null' + sep + 'null' + sep + 'null\n'
    return result


def test():
    ProducerThread().start()
    ConsumerThread().start()

if __name__ == '__main__':
    test()
