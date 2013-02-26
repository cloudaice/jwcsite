#-*-coding:utf-8-*-

import sys
sys.path.append(sys.path[0] + '/../../lib')
from bs4 import BeautifulSoup as BS
import escap
import requests
from pymongo import Connection
from gridfs import GridFS
db = Connection().images
fs = GridFS(db)


class Geren(object):
    def __init__(self, html):
        self.html = html
        self.soup = BS(html)
        self.student_num = None
        self.profile = {}

    def __call__(self):
        forms = self.soup.find('form')
        tbody = forms.find('tbody')
        if not tbody:
            tbody = forms.find('table')
            print tbody
        trs = filter(lambda x: hasattr(x, 'name') and x.name == 'tr', tbody.contents)
        for i, tr in enumerate(trs):
            if i == 6:
                continue
            tr_iter = tr.stripped_strings
            while True:
                try:
                    key = tr_iter.next()
                    if u'姓名拼音' in key:
                        key = key + tr_iter.next()
                    if i == 7:
                        value = tr.find('input').get('value')
                        print value
                    else:
                        value = tr_iter.next()
                    self.profile[key] = value
                except StopIteration:
                    break
        for key in self.profile.keys():
            print key, self.profile[key]
    
    def down_pic(self):
        try:
            r = requests.get(self.pic_url)
            assert(r.status_code == 200)
        except:
            return False
        oid = fs.put(myimage, content_type='image/jpeg', imagename=self.student_num)
        image = fs.get(oid).read()


if __name__ == "__main__":
    with open(current_dir + 'geren.html') as html:
        html = html.read()
        html = escap.escap(html)
        html = Geren(html)
    html()
