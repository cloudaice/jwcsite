#-*-coding:utf-8-*-
# @author: xianghcao<cloudaice@gmail.com>

from savedb import Savedb
from parse_geren import Geren


class CollectGeren(object):
    def __init__(self, req, stuid):
        html = req()
        docs = Geren(html)()
        Savedb(stuid, docs)()
