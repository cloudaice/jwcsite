#-*-coding: utf-8-*-

import sys
sys.path.append(sys.path[0] + '/../../')
import config
from factory import CollectGeren
from req import Get_html
from pymongo import Collection
import time

cnn = Collection('localhost', 27018, max_pool_size=10)
db = cnn['jwcsite']
table = db.PersonInfo

if __name__ == '__main__':
    stuids = table.find()
    for stuid in stuids:
        stuid = stuid['stuid']
        headers = config.headers_geren(stuid)
        url = config.url_geren
        req = Get_html(url, headers)
        collect = CollectGeren(req, stuid)
        time.sleep(0.5)
