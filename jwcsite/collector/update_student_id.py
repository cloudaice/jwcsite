#-*- coding: utf-8 -*-

"""
download student numbers to mongodb
"""

import sys
sys.path.append(sys.path[0] + '/../')
import config
import requests
from bs4 import BeautifulSoup as BS
from pymongo import Connection
cnn = Connection('localhost', 27018, max_pool_size=10)
db = cnn['jwcsite']
table = db.PersonInfo


def get_num(url):
    stu_nums = []
    r = requests.get(url)
    r.encoding = 'GBK'
    soup = BS(r.text)
    for link in soup.find_all('a'):
        num = link.get_text().strip().split('.')[0]
        try:
            int(num)
        except:
            continue
        stu_nums.append(link.get_text().strip().split('.')[0])
    print len(stu_nums)
    for num in stu_nums:
        condition = {'stuid': num}
        doc = {'stuid': num}
        table.update(condition, doc, upsert=True)

if __name__ == '__main__':
    urls = config.student_id_urls
    for url in urls:
        get_num(url)
