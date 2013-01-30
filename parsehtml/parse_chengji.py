#-*-coding:utf-8-*-
from bs4 import BeautifulSoup as BS
import re
import sys
import escap

current_dir = sys.path[0] + '/'

class Chengji(object):
    def __init__(self, html):
        self.html = html
        self.soup = BS(html)
        self.student_num = None
        self.chengji = []
        assert(self.soup.name == '[document]')


    def __call__(self):
       div = self.soup.html.find(id='spacemain').find(class_='center')
       div = filter(lambda x: hasattr(x, 'name') and x.name == 'table', div.contents)
       table = filter(lambda x: hasattr(x, 'name'), div[0].contents)
       self.student_num = table[0].stripped_strings.next().split()[0][0:-1]
      
       table = filter(lambda x: hasattr(x, 'name'), div[1].contents)
       table = filter(lambda x: hasattr(x, 'name'), table[1].contents)



if __name__ == "__main__":
    with open(current_dir + 'chengji.html', 'r') as html:
        html = html.read()
        html = escap.escap(html)
        html = Chengji(html)
    html()


