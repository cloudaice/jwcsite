#-*-coding:utf-8-*-

import tornado.web
import tornado.ioloop
import rule
from tornado.httpserver import HTTPServer


class RockHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            user_id = int(self.get_argument('user_id'))
            user_id = str(user_id)
        except:
            self.write({'code': '1000', 'message': 'user_id is not right'})
            return
        if not user_id:
            self.write({'code': '1001', 'message': 'user_id is none'})
            return

        rule_result = rule.Rule(user_id)
        rule_result.exec_rule()
        if rule_result.is_satisfy:
            prize = read_redis.get_prize('test_prize_pool')
            if prize is None or prize == 'None':
                self.write(rule_result.get_data())
            else:
                rule_result.warp_prize(prize)
                self.write(rule_result.get_data())
        else:
            #不满足规则，则返回相应的data
            self.write(rule_result.get_data())


class ValidateHandler(tornado.web.RequestHandler):
    def post(self):
        user_id = self.get_argument('user_id')
        product_id = self.get_argument('product_id')
        security_code = self.get_argument('security_code')
        try:
            user_id = int(user_id)
            user_id = str(user_id)
        except:
            self.write({'validate': 0})
            return 

        if validate.Validate(user_id, product_id, security_code):
            self.write({'validate': 1})
        else:
            self.write({'validate': 0})


class OrderHandler(tornado.web.RequestHandler):
    def post(self):
        user_id = self.get_argument('user_id')
        product_id = self.get_argument('product_id')
        security_code = self.get_argument('security_code')
        try:
            user_id = int(user_id)
            user_id = str(user_id)
        except:
            self.write({'validate': 0})
            return 
        self.write(order.Order(user_id, product_id, security_code))

class DelOrderHandler(tornado.web.RequestHandler):
    def post(self):
        user_id = self.get_argument('user_id')
        product_id = self.get_argument('product_id')
        security_code = self.get_argument('security_code')
        try:
            user_id = int(user_id)
            user_id = str(user_id)
        except:
            self.write({'validate': 0})
            return 
        self.write(order.Del_order(user_id, product_id, security_code))


application = tornado.web.Application([(r"/", Home),
                                       (r'/classroom', Classroom),
                                       (r'/feedback', Feedback),
                                       ], debug=True
                                      )

if __name__ == "__main__":
    http_server = HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
