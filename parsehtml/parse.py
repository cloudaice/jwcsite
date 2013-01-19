#-*-coding:utf-8-*-
from bs4 import BeautifulSoup as BS


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
        print self.soup.html.body.table


if __name__ == "__main__":
    fd = open('kb.html', 'r')
    html = kebiao(fd)
    #html._print()
    #html._findall('table')
    html._showtable()

