#-*-coding: utf-8-*-
# @author: xiangchao<cloudaice@gmail.com>

import logging
import logging.handlers
import os


def get_logger(filename):
    logger = logging.getLogger('jwcsite')
    handler = logging.FileHandler(filename)
    formatter = logging.Formatter('%(asctime)s - %(module)s.%(funcName)s.%(lineno)d - %(levelname)s - \
        %(message)s')
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger

logger = get_logger(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'jwcsite.log'))
namepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'jwcsite.log')
print os.path.abspath(__file__)
print os.path.dirname(os.path.abspath(__file__))
print namepath
