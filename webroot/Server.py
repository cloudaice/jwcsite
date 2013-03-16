#-*-coding:utf-8-*-

import sys
sys.path.append(sys.path[0] + '/../')
import os
from lib import Mongo
#import asyncmongo
import tornado.gen
import tornado.web
import tornado.ioloop
from tornado.httpserver import HTTPServer
from tornado.escape import json_encode

cnn = Mongo.conn()
db = cnn['jwcsite']


class Home(tornado.web.RequestHandler):
    def get(self):
        self.render('home.html')


class Classroom(tornado.web.RequestHandler):
    def get(self):
        self.render('classroom.html')

    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        date = self.get_argument('date')
        build = self.get_argument('build')
        param = self.get_argument('param')
        docs = yield tornado.gen.Task(self.get_data, date, build, param)
        self.write(json_encode(docs))
        self.finish()
    
    def get_data(self, date, build, param, callback=None):
        def selection(x):
            for i in param:
                if x['status'][int(i)] != '0':
                    return False
            if build not in x['roomname']:
                return False
            return True

        docs = db.Jiaoshi.find({'date': date}, {'roomname': 1, 'status': 1})
        docs = filter(selection, docs)
        docs = [doc['roomname'] for doc in docs]
        callback(docs)


class Curriculum(tornado.web.RequestHandler):
    def get(self):
        self.render('curriculum.html')

    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        query_string = self.get_argument('query_string').strip()
        docs = yield tornado.gen.Task(self.get_data, query_string)
        self.write(json_encode(docs))
        self.finish()
        
    def get_data(self, query_string, callback=None):
        docs = []
        cursor = db.Curriculum.find({"$or": [{'teacher': query_string}, {'course': query_string}]})
        for doc in cursor:
            del doc['_id']
            del doc['classId']
            if doc not in docs:
                docs.append(doc)
        callback(docs)


class About(tornado.web.RequestHandler):
    def get(self):
        self.render('about.html')


class Teac_Course(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        query_string = self.get_argument('query_string')
        docs = yield tornado.gen.Task(self.get_data, query_string)
        self.write(json_encode(docs))
        self.finish()

    def get_data(self, query_string, callback=None):
        docs = []
        cursor = db.Curriculum.find({}, {'teacher': 1, 'course': 1})
        for doc in cursor:
            if doc['teacher'] not in docs:
                docs.append(doc['teacher'])
            if doc['course'] not in docs:
                docs.append(doc['course'])
        docs = filter(lambda x: query_string in x, docs)
        if len(docs) > 8:
            docs = docs[:8]
        callback(docs)


settings = {
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'template_path': os.path.join(os.path.dirname(__file__), 'template'),
}


application = tornado.web.Application([(r'/', Home),
                                       (r'/classroom', Classroom),
                                       (r'/curriculum', Curriculum),
                                       (r'/Teac_Course', Teac_Course),
                                       (r'/about', About),
                                       (r'/favicon.ico', tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
                                       ], debug=True, **settings
                                      )

if __name__ == "__main__":
    port = int(sys.argv[1])
    http_server = HTTPServer(application)
    http_server.listen(port, '127.0.0.1')
    tornado.ioloop.IOLoop.instance().start()
