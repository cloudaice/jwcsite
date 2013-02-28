#-*-coding:utf-8-*-

import sys
sys.path.append(sys.path[0] + '/../')
import os
from lib import Mongo
#import asyncmongo
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

    def post(self):
        date = self.get_argument('date')
        section_start = int(self.get_argument('section_start'))
        section_end = int(self.get_argument('section_end'))
        docs = db.Jiaoshi.find({'date': date}, {'roomname': 1, 'status': 1})
        docs = filter(lambda x: x['status'][section_start - 1:section_end] == '0' * (section_end - section_start + 1), docs)
        for doc in docs:
            del doc['_id']
            del doc['status']
        self.write(json_encode(docs))


class Feedback(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        pass


settings = {
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'template_path': os.path.join(os.path.dirname(__file__), 'template'),
}


application = tornado.web.Application([(r'/', Home),
                                       (r'/classroom', Classroom),
                                       (r'/feedback', Feedback),
                                       (r'/favicon.ico', tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
                                       ], debug=True, **settings
                                      )

if __name__ == "__main__":
    http_server = HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
