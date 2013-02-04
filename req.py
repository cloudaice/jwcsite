#-*-coding: utf-8-*-
import requests
import sys
import config
sys.path.append(sys.path[0] + '/parse')


class Do_html(object):
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def __call__(self):
        r = requests.get(self.url, headers=self.headers)
        r.encoding = 'GBK'
        html = r.text
        return html


class Do_pic(object):
    def __init__(self, url):
        self.url = url

    def __call__(self):
        r = requests.get(url)
        name = url.split('/')[-1].strip()
        print name
        with open('image/' + name, 'w') as f:
            f.write(r.content)
            

if __name__ == '__main__':
    url = config.url_p
    down = Do_pic(url)
    down()
