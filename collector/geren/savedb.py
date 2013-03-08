#-*-coding: utf-8-*-

from pymongo import Connection

cnn = Connection('localhost', 27018, max_pool_size=10)
db = cnn['jwcsite']
table = db.PersonInfo


class Savedb(object):
    def __init__(self, stuid, docs):
        self.stuid = stuid
        self.docs = {}
        for doc in docs:
            if u'英文名' in doc:
                continue
            if u'教学班号' in doc:
                continue
            if u'本人' in doc:
                continue
            if u'专业' in doc:
                self.docs[u'专业'] = docs[doc].strip()
            else:
                self.docs[''.join(doc.strip().split())] = docs[doc].strip()

    def __call__(self):
        condition = {'stuid': self.stuid}
        self.docs['stuid'] = self.stuid
        table.update(condition, self.docs, upsert=True)
