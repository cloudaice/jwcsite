#-*-coding:utf-8-*-


class CollectJiaoshi(object):
    def __init__(self, week, campus):
        self.week = week
        self.campus = campus

    def __call__(self, req):
        html = req()
        docs = Jiaoshi(html)()
        save(self.week, self.campus, docs)

if __name__ == "__main__":
    pass

