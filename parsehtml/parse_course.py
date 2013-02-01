#-*-coding:utf-8-*-
from bs4 import BeautifulSoup as BS
import sys
import escap

current_dir = sys.path[0] + '/'
print current_dir


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
        for t in tables:
            print t.attrs


if __name__ == '__main__':
    with open(current_dir + 'xuanke.html') as html:
        html = html.read()
        html = escap.escap(html)
        html = Course(html)
    html()
    #html.show()
