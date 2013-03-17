# -*- coding: utf-8 -*-

import sys
sys.path.append(sys.path[0] + '/../../')
import config
from factory import CollectJiaoshi
from req import Post_html
from datetime import datetime


def wrapweek(week):
    if week < 10:
        return '0' + str(week)
    else:
        return str(week)

if __name__ == '__main__':
    tern_start_day = config.tern_start_day
    tern_start_day = [int(v) for v in tern_start_day.split('-')]
    d1 = datetime(tern_start_day[0], tern_start_day[1], tern_start_day[2])
    d2 = datetime.now()
    days = (d2 - d1).days
    week = wrapweek(((days) / 7 + 2))
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
    collect(req)
