# -*- coding: utf-8 -*-
import sys
sys.path.append(sys.path[0] + '/parse')
from parse_jiaoshi import Jiaoshi
import config
from req import *


if __name__ == '__main__':
    week = '01'
    campus = '一校区'
    collect = CollectJiaoshi(week, campus)
    parame = {'JS': '',
              'ZC': week,
              'XQ': campus.decode('utf-8').encode('gb2312'),
              'submit2': '全部浏览'.decode('utf-8').encode('gb2312')
              }
    url = config.url_jiaoshi
    headers = config.headers_chengji
    req = Post_html(url, headers, parame)
    parse = Jiaoshi()
    save = savedb()

