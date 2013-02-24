#-*-coding: utf-8 -*-
from bs4 import BeautifulSoup as BS
import sys
sys.path.append(sys.path[0] + '/../')
import datetime
import config
import Mongo

current_dir = sys.path[0] + '/'
cnn = Mongo.conn()
db = cnn['jwcsite']


def add_day(start_date, adder):
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    delta = datetime.timedelta(days=adder)
    result_date = start_date + delta
    return result_date.strftime('%Y-%m-%d')


class Jiaoshi(object):
    def __init__(self, html):
        self.html = html
        self.soup = BS(html)
        self.rooms = []
        assert(self.soup.name == '[document]')

    def __call__(self):
        div = self.soup.html.find(id='spacemain').find(class_='center')
        table = div.find('table', bgcolor='#FFFFFF')
        table = filter(lambda x: hasattr(x, 'name'), table.contents)
        for row in table[2:]:
            tds = filter(lambda x: hasattr(x, 'name') and x.name == 'td', row.contents)
            room_name = tds[0].string.strip()
            all_colors = []
            for td in tds[1:]:
                all_colors.append(td.get('bgcolor'))
            week_status = ''.join(['0' if color == '#FFFFFF' else '1' for color in all_colors])
            self.rooms.append((room_name, week_status))

    def show(self):
        for room, status in self.rooms:
            print room, status

    def save_database(self, week):
        week = int(week)
        tern_start_day = config.tern_start_day
        week_start_date = add_day(tern_start_day, week * 7)
        docs = []
        for room, status in self.rooms:
            doc = {'roomname': room, 'campus': '一校区'}


        for doc in docs:

            
            
            
