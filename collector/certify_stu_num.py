#-*-coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as BS

"""
用于过滤采集到的学号，把错误的学号过滤掉
"""


def get_stu():
    url = 'http://xscj.hit.edu.cn/HitJwGL/ZYPY/ZYJS.ASP'
    yuanxi_nums = []
    r = requests.get(url)
    r.encoding = 'GBK'
    soup = BS(r.text)
    table = soup.find_all('table', border='1')
    trs = filter(lambda x: hasattr(x, 'name') and x.name == 'tr', table[0].contents)

    for line in trs:
        for string in line.stripped_strings:
            try:
                int(string)
                if len(string) == 3:
                    yuanxi_nums.append(string)
            except:
                continue
    
    for num in yuanxi_nums:
        print num
    print len(yuanxi_nums)
    return yuanxi_nums
