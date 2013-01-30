#-*-coding:utf-8-*-
from bs4 import BeautifulSoup as BS
import re
import sys
import escap


class Chengji(object):
    def __init__(self, html):
        self.html = html
        self.soup = BS(html)
        self.table_title = None

    def __call__(self):
        pass

