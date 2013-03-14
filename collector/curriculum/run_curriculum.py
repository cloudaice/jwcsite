# -*- coding: utf-8 -*-
import sys
sys.path.append(sys.path[0] + '/../../')
import config
from factory import CollectCurriculum
from req import Post_html

if __name__ == "__main__":
    classId = ''
    headers = config.headers_kb
    url = config.url_kb

