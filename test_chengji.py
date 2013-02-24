# -*-coding: utf-8 -*-

import sys
sys.path.append(sys.path[0] + '/parse')
import config
from  parse_chengji import Chengji
from req import *

if __name__ == '__main__':
    url = config.url_chengji
    headers = config.headers_chengji
    parame = {'selectXQ': 'all',
              'LB': '1',
              'Submit': '查询成绩'
              }
    down = Post_html(url, headers, parame)
    html = down()
    html = Chengji(html)
    html()
    html.show()
