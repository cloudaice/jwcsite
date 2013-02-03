#-*-coding: utf-8-*-
import requests
import sys
import config
sys.path.append(sys.path[0] + '/parsehtml')
import parse_geren

if __name__ == '__main__':
    url = config.url
    headers = config.headers
    r = requests.post(url, headers=headers)
    r.encoding = 'GBK'
    html = r.text
    html = parse_geren.Geren(html)
    html()
