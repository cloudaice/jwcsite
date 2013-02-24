#-*-coding: utf-8 -*-
from bs4 import BeautifulSoup as BS
import sys

current_dir = sys.path[0] + '/'


class Jiaoshi(object):
    def __init__(self, html):
        self.html = html
        self.soup = BS(html)
        self.rooms = []
        assert(self.soup.name == '[document]')

    def __call__(self):
        div = self.soup.html.find(id='spacemain').find(class_='center')
        table = div.find('table', bgcolor='#FFFFFF')
        print table
