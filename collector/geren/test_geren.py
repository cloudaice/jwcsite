#-*-coding: utf-8-*-

import sys
sys.path.append(sys.path[0] + '/../../')
import config
from factory import CollectGeren
from req import Get_html

if __name__ == '__main__':
    headers = config.headers_geren('1090310108')
    url = config.url_geren
    req = Get_html(url, headers)
    collect = CollectGeren(req, '1090310108')
