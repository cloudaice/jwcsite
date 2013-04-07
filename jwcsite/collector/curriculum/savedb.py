# -*- coding: utf-8 -*-

from pymongo import Connection

cnn = Connection('localhost', 27018, max_pool_size=10)
db = cnn['jwcsite']
table = db.Curriculum


class Savedb(object):
    def __init__(self, classId, docs):
        self.classId = classId
        self.docs = docs

    def __call__(self):
        for doc in self.docs:
            doc['classId'] = self.classId
            table.update(doc, doc, upsert=True)
