# -*- coding: utf-8 -*-

from savedb import Savedb
from parse_curriculum import Curriculum


class CollectCurriculum(object):
    def __init__(self, classId):
        self.classId = classId

    def __call__(self, req):
        html = req()
        docs = Curriculum(html)()
        print docs
        #Savedb(self.classId, docs)()
