#-*-coding:utf-8-*-

from savedb import Savedb
from parse_geren import Geren


class CollectGeren(object):
    def __init__(self, req):
        html = req()
        docs = Geren(html)()
        Savedb(docs)()
