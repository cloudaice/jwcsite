# -*- coding: utf-8 -*-
import sys
sys.path.append(sys.path[0] + '/../../')
import config
from factory import CollectCurriculum
from req import Post_html
from pymongo import Connection
import time

cnn = Connection('localhost', 27018, max_pool_size=10)
db = cnn['jwcsite']
table = db.PersonInfo


if __name__ == "__main__":
    all_classId = []
    headers = config.headers_kb
    url = config.url_kb
    stuids = table.find({}, {'stuids': 1})
    for stuid in stuids:
        classId = stuid['stuid'].strip()[1:8]
        if classId in all_classId:
            continue
        all_classId.append(classId)
        params = {'BH': classId,
                  'submit': '查询课表'.decode('utf-8').encode('gb2312')
                  }
        collect = CollectCurriculum(classId)
        req = Post_html(url, headers, params)
        try:
            collect(req)
        except:
            continue
        time.sleep(0.5)
