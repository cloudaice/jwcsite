#-*-coding:utf-8-*-
# @author: xiangchao<cloudaice@gmail.com>

import sys
sys.path.append(sys.path[0] + '/../../')
from bs4 import BeautifulSoup as BS


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
        
        try:
            self.student_num = table[0].stripped_strings.next().split()[0][0:-1]
        except StopIteration:
            print 'can not get student number'
            pass

        table = filter(lambda x: hasattr(x, 'name'), div[1].contents)
        for row in table:
            this_row = ['' for _ in range(10)]
            row_iter = row.stripped_strings
            try:
                tern = row_iter.next()
            except StopIteration:
                continue
            this_row[0] = tern
            for i in range(1, 10, 1):
                try:
                    this_row[i] = row_iter.next()
                except StopIteration:
                    continue
            self.chengji.append(tuple(this_row))

    def show(self):
        print self.student_num
        for row in self.chengji:
            print "%s," * 10 % row
