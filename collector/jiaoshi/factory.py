#-*-coding:utf-8-*-



class CollectJiaoshi(object):
    def __init__(self, week, campus):
        self.week = week
        self.campus = campus

    def __call__(self,req, parse, save):
        



if __name__ == "__main__":
    week = '01'
    campus = '一校区'
    collect = CollectJiaoshi(week, campus)
    collect()


        
