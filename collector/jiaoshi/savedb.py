#-*-coding: utf-8-*-


cnn = Mongo.conn()
db = cnn['jwcsite']
table = db.Jiaoshi

def add_day(start_date, adder):
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    delta = datetime.timedelta(days=adder)
    result_date = start_date + delta
    return result_date.strftime('%Y-%m-%d')


class Savedb(object):
    def __init__(self, week, campus, data):
        week = int(week)
        tern_start_day = config.tern_start_day
        week_start_date = add_day(tern_start_day, week * 7)
        self.docs = []
        for room, status in rooms:
            #把status字符串按照5个5个进行切分
            status = map(lambda x, y: status[x:y], range(0, 35, 5), range(5, 40, 5))
            for i, state in enumerate(status):
                doc = {'roomname': room, 'campus': campus,
                        'date': add_day(tern_start_day, week * 7 + i),
                        'status': state
                        }
                docs.append(doc)


    def __call__(self):
        for doc in docs:
            condition = {'roomname': doc['roomname'],
                         'campus': doc['campus'],
                         'date': doc['date']
                         }
            table.update(condition, doc, upsert=True)

