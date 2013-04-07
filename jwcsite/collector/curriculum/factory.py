# -*- coding: utf-8 -*-
# @author: xiangchao<cloudaice@gmail.com>

from savedb import Savedb
from parse_curriculum import Curriculum


class CollectCurriculum(object):
    def __init__(self, classId):
        self.classId = classId

    def __call__(self, req):
        html = req()
        docs = Curriculum(html)()
        Savedb(self.classId, docs)()
