# -*- coding: utf-8 -*-
import sys
sys.path.append(sys.path[0] + '/parse')
from parse_jiaoshi import Jiaoshi
import config
from req import *


if __name__ == '__main__':
    parame = {'JS': '',
              'ZC': '01',
              'XQ': '一校区'.decode('utf-8').encode('gb2312'),
              'submit2': '全部浏览'.decode('utf-8').encode('gb2312')
              }
    url = config.url_jiaoshi
    headers = config.headers_chengji
    down = Post_html(url, headers, parame)
    html = down()
    html = Jiaoshi(html)
    html()

