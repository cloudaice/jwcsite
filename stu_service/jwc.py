#*- coding: utf-8 -*-
from HTMLParser import HTMLParser
from htmlentitydefs import entitydefs
import cookielib
import urllib
import urllib2
import re
import sys


class jwc():
    def __init__(self):
        self.data=''
        self.parameter={}
        self.url_login=''
        self.typename=''

    def set_coolie():
        cj = cookielib.LWPCookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)

    def set_kb(self,bj):
        self.typename='kb'
        self.parameter = {
                'BH': bj,
                'submit': '查询课表'.decode('utf-8').encode('gb2312')
                }
        self.url_login = "http://xscj.hit.edu.cn/HitJwgl/XS/kfxqkb.asp"

    def set_js(self,week,area):
        self.typename='js'
        self.parameter = {
        'JS': '',
        'ZC': week,
        'XQ': area.decode('utf-8').encode('gb2312'),
        'submit2': '全部浏览'.decode('utf-8').encode('gb2312')
                   }
        self.url_login = "http://xscj.hit.edu.cn/HitJwgl/XS/kfjscx_all.asp"


    def get_html(self):
        req = urllib2.Request(
                self.url_login, urllib.urlencode(self.parameter)
                )
        jump = urllib2.urlopen(req)
        data = jump.read()
        data=data.decode('gb2312','ignore').encode('utf-8')
        return data

    def view_data(self): 
        data=self.get_html()
        if self.typename=='kb':
            if '系统提示' in data:
                return None
            data = re.sub('gb2312','utf-8',data) #将'gb2312'替换成'utf-8'
            data = re.sub('<td><strong class="STYLE1">学期课表查询</strong></td>','',data) 
            data = re.sub('<td><div align="right"><a href="KFxqkb.asp" >查询其他班级课表</a></div></td>','',data) 
            data = re.sub('<LI><A class=menu href="Http://Jwc.Hit.Edu.Cn"><SPAN>返回教务处主页</SPAN></A></LI>',
                    '<LI><A href="/"><SPAN>返回首页</SPAN></A></LI>',data) 
        self.data=data
        return self.data

    def into_file(self,filename):
        self.data=self.view_data()
        f = open(filename,'w')
        f.write(self.data)


class jsparser(HTMLParser):
    def __init__(self):
        self.js_in=0                        #记录一个<tr>中读取到哪一行
        self.js=[]                          #存储教室名字的列表 
        self.status=[]                      #存储每一个教室一个星期的使用状态，因此，它是一个双层列表
        self.js_status=[]                   #一个教室一个星期的使用状态，它作为self.status的一个元素
        self.js_data=''                     #计算教室名字的中间量
        HTMLParser.__init__(self)           #初始化父类

    def handle_starttag(self,tag,attrs):  #读到开始标签
        if tag == 'td' and len(attrs) == 1:
            name,value = attrs[0]
            if name == 'height' and value == '20':    #判定是教室名字的标签
                self.js_in =1

            if name == 'bgcolor' and self.js_in:      #判断是教室使用状态的标签
                self.js_status.append(value)
                self.js_in+=1

                    
    def handle_data(self,data):      #记录教室名字
        if self.js_in == 1:
            self.js_data+=data
            
    def handle_endtag(self,tag):      #读到结尾标签
        if tag == 'td' and self.js_in==1:   
            "判断是教室名字结尾标签,存储名字，并且清空中间变量self.js_data"
            self.js.append(self.js_data)
            self.js_data=''
        if tag == 'td' and self.js_in == 36:
            "判断读取教室状态标签完结"
            self.js_in =0
            self.status.append(self.js_status)
            self.js_status=[]
    '''
    用来处理html中的实体的值的，在这里没有什么用处
    def handle_entityref(self,name):
        if entitydefs.has_key(name):
            self.handle_data(entitydefs[name])
        else:
            self.handle_data('&' + name + ';')
    '''
    def getresult(self):    #打印结果
        for key in range(len(self.js)):
            self.js[key]="".join(self.js[key].split())
            sys.stdout.write("%s    " % self.js[key]) 
            # for value in self.status[key]:
            #    sys.stdout.write("%s " % (self.color_to_value(value)))
            sys.stdout.write(' '.join(self.color_to_value(value) for value in self.status[key]))
            sys.stdout.write("\n")
        print len(self.js)

    def get_room(self):
        for key in range(len(self.js)):
            self.js[key]="".join(self.js[key].split())
        return self.js

    def get_status(self):
        status=[]
        for key in range(len(self.js)):
            status.append(''.join(self.color_to_value(value) for value in self.status[key]) )
        return status
        

    def color_to_value(self,color):
        if color == '#FFFFFF':
            return '0'
        if color == '#0000FF':
            return '1'
        if color == "#FF0000":
            return '2'

if __name__ == '__main__':
    #bj = '0903101'
    #filename = 'kb.html'
    newpage = jwc()
    #newpage.set_kb(bj)
    #print newpage.view_data()
    newpage.set_js('09','一校区')
    tp = jsparser()
    tp.feed(newpage.view_data())
    tp.getresult()
    s=tp.get_status()
    for key in s:
        print key
