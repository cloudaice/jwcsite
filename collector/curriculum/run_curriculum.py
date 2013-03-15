# -*- coding: utf-8 -*-
import sys
sys.path.append(sys.path[0] + '/../../')
import config
from factory import CollectCurriculum
from req import Post_html

if __name__ == "__main__":
    classId = '1103101'
    collect = CollectCurriculum(classId)
    headers = config.headers_kb
    url = config.url_kb
    params = {'BH': classId,
              'submit': '查询课表'.decode('utf-8').encode('gb2312')
              }
    req = Post_html(url, headers, params)
    collect(req)
