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


if __name__ == '__main__':
    with open(current_dir + 'xuanke.html') as html:
        html = html.read()
        html = escap.escap(html)
        html = Course(html)
    html()
    html.show()

