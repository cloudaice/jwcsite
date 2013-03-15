# -*- coding: utf-8 -*-

from savedb import Savedb
from parse_curriculum import Curriculum


class CollectCurriculum(object):
    def __init__(self, classId):
        self.classId = classId

    def __call__(self, req):
        html = req()
        docs = Curriculum(html)()
        for doc in docs:
            print doc['weekday'], doc['section'], doc['course'], doc['teacher'], doc['addr'], doc['startend']
        #Savedb(self.classId, docs)()
