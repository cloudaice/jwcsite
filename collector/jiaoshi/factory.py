#-*-coding:utf-8-*-

from savedb import Savedb
from parse_jiaoshi import Jiaoshi


class CollectJiaoshi(object):
    def __init__(self, week, campus):
        self.week = week
        self.campus = campus

    def __call__(self, req):
        html = req()
        docs = Jiaoshi(html)()
        Savedb(self.week, self.campus, docs)
