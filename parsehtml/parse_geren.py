#-*-coding:utf-8-*-
from bs4 import BeautifulSoup as BS
import sys
import escap
current_dir = sys.path[0] + '/'


class Geren(object):
    def __init__(self, html):
        self.html = html
        self.soup = BS(html)
        self.student_num = None
        self.profile = []

    def __call__(self):
        forms = self.soup.find('form')
        tbody = forms.find('tbody')
        trs = filter(lambda x: hasattr(x, 'name') and x.name == 'tr', tbody.contents)

if __name__ == "__main__":
    with open(current_dir + 'geren.html') as html:
        html = html.read()
        html = escap.escap(html)
        html = Geren(html)
    html()
