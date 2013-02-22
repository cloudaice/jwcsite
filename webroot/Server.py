#-*-coding:utf-8-*-

import os
import Mongo
import asyncmongo
import tornado.web
import tornado.ioloop
from tornado.httpserver import HTTPServer

cnn = Mongo.conn()
db = cnn['jwcsite']

class Home(tornado.web.RequestHandler):
    def get(self):
        self.render('home.html')


class Classroom(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        date = self.get_argument('date')
        section_start = self.get_argument('section_start')
        section_end = self.get_argument('sections_end')
        docs = db.ClassStatus.find({'date':date}, {'roomname': 1, 'status': 1})
        docs = filter(lambda x: x['status'][section_start-1:section_end] == '0' * (section_end - section_start + 1), docs)
        self.render('home.html', room_table = docs)


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
                                       ], debug=True, **settings
                                      )

if __name__ == "__main__":
    http_server = HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
