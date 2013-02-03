#-*-coding: utf-8-*-
import requests
import sys
import config
sys.path.append(sys.path[0] + '/parsehtml')
import parse_geren


class Do_html(object):
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def __call__(self):
        r = requests.post(url, headers=headers)
        r.encoding = 'GBK'
        html = r.text
        return html

class Do_pic(object):
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def __call__(self):
        r = requests.post(url, headers=headers)

if __name__ == '__main__':
    url = config.url
    headers = config.headers
    r = requests.post(url, headers=headers)
    r.encoding = 'GBK'
    html = r.text
    html = parse_geren.Geren(html)
    html()

