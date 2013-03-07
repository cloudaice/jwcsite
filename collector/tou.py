#-*- coding: utf-8 -*-

"""
download student numbers to mongodb
"""

import requests
from bs4 import BeautifulSoup as BS
from pymongo import Connection
import certify_stu_num
cnn = Connection('localhost', 27017, max_pool_size=10)
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
        print num
        print num[3:6]
    faculty = certify_stu_num.get_stu()
    stu_nums = filter(lambda x: x[3:6] in faculty, stu_nums)
    
    print len(stu_nums)
    #for num in ]tu_nums:
    #    condition = {'stuid': num}
    #    doc = {'stuid': num}
    #    table.update(condition, doc, upsert=True)

if __name__ == '__main__':
    urls = ['http://xscj.hit.edu.cn/hitjwgl/XS/XSZP/zp109/',
            'http://xscj.hit.edu.cn/hitjwgl/XS/XSZP/zp110/',
            'http://xscj.hit.edu.cn/hitjwgl/XS/XSZP/zp111/',
            'http://xscj.hit.edu.cn/hitjwgl/XS/XSZP/zp112/'
            ]
    for url in urls:
        get_num(url)
