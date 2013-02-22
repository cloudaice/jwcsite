#-*-coding:utf-8-*-

import tornado.web
import tornado.ioloop
from tornado.httpserver import HTTPServer


class Home(tornado.web.RequestHandler):
    def get(self):
        pass


class Classroom(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        pass


class Feedback(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        pass


application = tornado.web.Application([(r"/", Home),
                                       (r'/classroom', Classroom),
                                       (r'/feedback', Feedback),
                                       ], debug=True
                                      )

if __name__ == "__main__":
    http_server = HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
