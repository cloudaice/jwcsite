#-*-coding: utf-8-*-
# @author: xiangchao<cloudaice@gmail.com>

import requests
import sys
sys.path.append(sys.path[0] + '/../../')


class Get_html(object):
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def __call__(self):
        r = requests.get(self.url, headers=self.headers)
        r.encoding = 'GBK'
        html = r.text
        return html


class Post_html(object):
    def __init__(self, url, headers, parame):
        self.url = url
        self.headers = headers
        self.parame = parame

    def __call__(self):
        r = requests.post(self.url, data=self.parame, headers=self.headers)
        r.encoding = 'GBK'
        html = r.text
        return html
    

class Do_pic(object):
    def __init__(self, url):
        self.url = url

    def __call__(self):
        try:
            r = requests.get(self.url)
            assert(r.status_code == 200)
            name = self.url.split('/')[-1].strip()
        except:
            return False
        with open('image/' + name, 'w') as f:
            f.write(r.content)
        return True
            
if __name__ == '__main__':
    pass
