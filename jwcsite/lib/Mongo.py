#-*-coding:utf-8-*-

from pymongo import Connection
cnn = None


def conn():
    """
    Mongodb connections pool
    """
    global cnn
    if cnn is None:
        cnn = Connection('localhost', 27018, max_pool_size=10)
    return cnn
