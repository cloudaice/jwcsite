#-*-coding:utf-8-*-
# @author: xiangchao<cloudaice@gmail.com>

import sys
sys.path.append(sys.path[0] + '/../../lib')
from bs4 import BeautifulSoup as BS
import escap

current_dir = sys.path[0] + '/'
print current_dir

"""
tuple
('课程名','授课教师','学分','学时','起止周','详细信息','上课时间','教室','备注')

"""


class Course(object):
    def __init__(self, html):
        self.html = html
        self.course = []
        self.soup = BS(html)
        assert(self.soup.name == '[document]')
    
    def __call__(self):
        tbody = self.soup.html.find(id='spacemain').find(class_='center').find(align='center')
        tbody = filter(lambda x: hasattr(x, 'name') and x.name == 'tbody', tbody.contents)[0]
        trs = filter(lambda x: hasattr(x, 'name') and x.name == 'tr', tbody.contents)
        td = filter(lambda x: hasattr(x, 'name'), trs[1].contents)[0]
        tables = filter(lambda x: hasattr(x, 'name') and x.name == 'table'
                        and x.get('align') and x['align'] == 'center', td.contents)
        for table in tables:
            tbody = table.find('tbody', recursive=False)
            trs = filter(lambda x: hasattr(x, 'name'), tbody.find_all('tr', recursive=False))
            for tr in trs:
                tr_iter = tr.stripped_strings
                while True:
                    try:
                        print tr_iter.next(),
                    except StopIteration:
                        break
                print '\n'

if __name__ == '__main__':
    with open(current_dir + '../htmls/xuanke.html') as html:
        html = html.read()
        html = escap.escap(html)
        html = Course(html)
    html()
    #html.show()
