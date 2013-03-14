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
        build = self.get_argument('build')
        param = self.get_argument('param')

        def escap(x):
            for i in param:
                if x['status'][int(i)] != '0':
                    return False
            if build not in x['roomname']:
                return False
            return True

        docs = db.Jiaoshi.find({'date': date}, {'roomname': 1, 'status': 1})
        docs = filter(escap, docs)
        docs = [doc['roomname'] for doc in docs]
        self.write(json_encode(docs))


class About(tornado.web.RequestHandler):
    def get(self):
        self.render('about.html')


settings = {
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'template_path': os.path.join(os.path.dirname(__file__), 'template'),
}


application = tornado.web.Application([(r'/', Home),
                                       (r'/classroom', Classroom),
                                       (r'/about', About),
                                       (r'/favicon.ico', tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
                                       ], debug=True, **settings
                                      )

if __name__ == "__main__":
    port = int(sys.argv[1])
    http_server = HTTPServer(application)
    http_server.listen(port, '127.0.0.1')
    tornado.ioloop.IOLoop.instance().start()
