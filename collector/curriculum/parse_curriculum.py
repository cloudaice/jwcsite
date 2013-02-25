#-*-coding:utf-8-*-

import sys
sys.path.append(sya.path[0] + '/../../lib')
from bs4 import BeautifulSoup as BS

current_dir = sys.path[0] + '/'
print current_dir


class Kebiao(object):
    def __init__(self, html):
        self.html = html
        self.soup = BS(html)
        self.table_title = None
        # self.kebiao data struct like: [[(课程名, 教师教室, 上课周次),...],[...],...]
        self.kebiao = [[[] for i in range(6)] for j in range(8)]
        # self.exams data struct like: [(周次, 星期, 时间, 地点, 课程名), ...]
        self.exams = []
        self.weekdays_name = []
        assert(self.soup.name == '[document]')

    def _print(self):
        print self.soup.prettify()

    def __call__(self):
        div = self.soup.html.body.find(id='spacemain').find(class_='center')
        table = filter(lambda x: hasattr(x, 'name') and x.name == 'table', div.contents)
        table = filter(lambda x: hasattr(x, 'name'), table[1].contents)
        table = filter(lambda x: hasattr(x, 'name'), table[0].contents)
        table = filter(lambda x: hasattr(x, 'name'), table[1].contents)
        self.table_title = [string for string in table[0].stripped_strings][0]

        # row 为整张表格
        row = filter(lambda x: hasattr(x, 'name'), table[1].contents)

        # 获取课表中的每一行
        kb_title = filter(lambda x: hasattr(x, 'name'), row[0].contents)
        kb_first_class = filter(lambda x: hasattr(x, 'name'), row[1].contents)
        kb_second_class = filter(lambda x: hasattr(x, 'name'), row[2].contents)
        kb_third_class = filter(lambda x: hasattr(x, 'name'), row[3].contents)
        kb_forth_class = filter(lambda x: hasattr(x, 'name'), row[4].contents)
        kb_fifth_class = filter(lambda x: hasattr(x, 'name'), row[5].contents)
        kb_exam = filter(lambda x: hasattr(x, 'name'), row[6].contents)

        # 提取课表项：周一,周二....
        self.weekdays_name = []
        for kb_t in kb_title[1:]:
            try:
                self.weekdays_name.append(kb_t.stripped_strings.next())
            except StopIteration:
                pass

        # 提取第一节课的信息
        for i, kb_f in enumerate(kb_first_class[1:]):
            tmp = filter(lambda x: hasattr(x, 'name'), kb_f.contents)
            ts = tmp[0].stripped_strings
            tmp = filter(lambda x: hasattr(x, 'name'), tmp[0].contents)
            while True:
                try:
                    self.kebiao[i + 1][1].append((ts.next(), ts.next(), ts.next()))
                except StopIteration:
                    break

        # 提取第二节
        for i, kb_s in enumerate(kb_second_class[1:]):
            tmp = filter(lambda x: hasattr(x, 'name'), kb_s.contents)
            ts = tmp[0].stripped_strings
            while True:
                try:
                    self.kebiao[i + 1][2].append((ts.next(), ts.next(), ts.next()))
                except StopIteration:
                    break

        # 提取第三节课
        for i, kb_t in enumerate(kb_third_class[1:]):
            tmp = filter(lambda x: hasattr(x, 'name'), kb_t.contents)
            ts = tmp[0].stripped_strings
            while True:
                try:
                    self.kebiao[i + 1][3].append((ts.next(), ts.next(), ts.next()))
                except StopIteration:
                    break

        # 提取第四节课
        for i, kb_f in enumerate(kb_forth_class[1:]):
            tmp = filter(lambda x: hasattr(x, 'name'), kb_f.contents)
            ts = tmp[0].stripped_strings
            while True:
                try:
                    self.kebiao[i + 1][4].append((ts.next(), ts.next(), ts.next()))
                except StopIteration:
                    break

        # 提取第五节课
        for i, kb_f in enumerate(kb_fifth_class[1:]):
            tmp = filter(lambda x: hasattr(x, 'name'), kb_f.contents)
            ts = tmp[0].stripped_strings
            while True:
                try:
                    self.kebiao[i + 1][5].append((ts.next(), ts.next(), ts.next()))
                except StopIteration:
                    break

        #考试信息提取
        for i, kb_e in enumerate(kb_exam[1:]):
            tmp = filter(lambda x: hasattr(x, 'name'), kb_e.contents)
            ts = tmp[0].stripped_strings
            for text in ts:
                self.exams.append(tuple(text.split()))

    def showtable(self):
        for i in range(1, 8, 1):
            print self.weekdays_name[i - 1], ':'
            for j in range(1, 6, 1):
                print "第%d节:" % j,
                for course, teac_and_addr, weeks in self.kebiao[i][j]:
                    print course, teac_and_addr, weeks,
                print '\n'
        for week, day, time, addr, course in self.exams:
            print week, day, time, addr, course


if __name__ == "__main__":
    with open(current_dir + 'kb.html', 'r') as html:
        html = Kebiao(html)
    html()
    html.showtable()
