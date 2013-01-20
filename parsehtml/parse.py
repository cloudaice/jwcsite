#-*-coding:utf-8-*-
from bs4 import BeautifulSoup as BS
import re


class kebiao(object):
    def __init__(self, html):
        self.html = html
        self.soup = BS(html)
        assert(self.soup.name == '[document]')

    def _print(self):
        print self.soup.prettify()

    def _findall(self, tag):
        tags = self.soup.find_all(tag)
        for t in tags:
            print len(t.contents)

    def _showtable(self):
        div = self.soup.html.body.find(id='spacemain').find(class_='center')
        table = div.find_all(border='0')[1]
        print table.name
        print len(table.contents)
        for child in table.children:
            if hasattr(child, 'name'):
                print child.name
                print child
                print '##################'

        exit()
        print len(table)
        for content in  table:
            if hasattr(content, 'name'):
                print content.name


if __name__ == "__main__":
    fd = open('kb.html', 'r')
    html = kebiao(fd)
    #html._print()
    #html._findall('table')
    html._showtable()

