#@+leo-ver=5-thin
#@+node:cloudaice.20120216102454.1139: * @file /home/cloudaice/pyrepo/jwcsite/stu_service/jwc.py
#@@language python
#@@tabwidth -4
#@+others
#@+node:cloudaice.20120216102454.1140: ** jwc declarations
# -*- coding: utf-8 -*-
from HTMLParser import HTMLParser
from htmlentitydefs import entitydefs
import cookielib
import urllib
import urllib2
import re
import sys


#@+node:cloudaice.20120216102454.1141: ** class jwc
class jwc():
    #@+others
    #@+node:cloudaice.20120216102454.1142: *3* __init__
    def __init__(self):
        self.data=''
        self.parameter={}
        self.url_login=''
        self.typename=''

    #@+node:cloudaice.20120216102454.1143: *3* set_coolie
    def set_coolie():
        cj = cookielib.LWPCookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)

    #@+node:cloudaice.20120216102454.1144: *3* set_kb
    def set_kb(self,bj):
        self.typename='kb'
        self.parameter = {
                'BH': bj,
                'submit': '查询课表'.decode('utf-8').encode('gb2312')
                }
        self.url_login = "http://xscj.hit.edu.cn/HitJwgl/XS/kfxqkb.asp"

    #@+node:cloudaice.20120216102454.1145: *3* set_js
    def set_js(self,week,area):
        self.typename='js'
        self.parameter = {
        'JS': '',
        'ZC': week,
        'XQ': area.decode('utf-8').encode('gb2312'),
        'submit2': '全部浏览'.decode('utf-8').encode('gb2312')
                   }
        self.url_login = "http://xscj.hit.edu.cn/HitJwgl/XS/kfjscx_all.asp"


    #@+node:cloudaice.20120216102454.1146: *3* get_html
    def get_html(self):
        req = urllib2.Request(
                self.url_login,
                urllib.urlencode(self.parameter)
                )
        jump = urllib2.urlopen(req)
        data = jump.read()
        data=data.decode('gb2312').encode('utf-8')
        return data

    #@+node:cloudaice.20120216102454.1147: *3* view_data
    def view_data(self): 
        data = self.get_html()
        if self.typename=='kb':
            data = re.sub('gb2312','utf-8',data) #将'gb2312'替换成'utf-8'
        self.data=data
        return self.data

    #@+node:cloudaice.20120216102454.1148: *3* into_file
    def into_file(self,filename):
        self.data=self.view_data()
        f = open(filename,'w')
        f.write(self.data)


    #@-others
#@+node:cloudaice.20120216102454.1149: ** class jsparser
class jsparser(HTMLParser):
    #@+others
    #@+node:cloudaice.20120216102454.1150: *3* __init__
    def __init__(self):
        self.js_in=0    #记录一个<tr>中读取到哪一行
        self.js=[]    #存储教室名字的列表 
        self.status=[]    #存储每一个教室一个星期的使用状态，因此，它是一个双层列表
        self.js_status=[]    #一个教室一个星期的使用状态，它作为self.status的一个元素
        self.js_data=''    #计算教室名字的中间量
        HTMLParser.__init__(self)    #初始化父类

    #@+node:cloudaice.20120216102454.1151: *3* handle_starttag
    def handle_starttag(self,tag,attrs):  #读到开始标签
        if tag == 'td' and len(attrs) == 1:
            name,value = attrs[0]
            if name == 'height' and value == '20':    #判定是教室名字的标签
                self.js_in =1

            if name == 'bgcolor' and self.js_in:      #判断是教室使用状态的标签
                self.js_status.append(value)
                self.js_in+=1

                    
    #@+node:cloudaice.20120216102454.1152: *3* handle_data
    def handle_data(self,data):      #记录教室名字
        if self.js_in == 1:
            self.js_data+=data
            
    #@+node:cloudaice.20120216102454.1153: *3* handle_endtag
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
    #@+node:cloudaice.20120216102454.1154: *3* getresult
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

    #@+node:cloudaice.20120216102454.1155: *3* get_room
    def get_room(self):
        for key in range(len(self.js)):
            self.js[key]="".join(self.js[key].split())
        return self.js

    #@+node:cloudaice.20120216102454.1156: *3* get_status
    def get_status(self):
        status=[]
        for key in range(len(self.js)):
            status.append(''.join(self.color_to_value(value) for value in self.status[key]) )
        return status
        

    #@+node:cloudaice.20120216102454.1157: *3* color_to_value
    def color_to_value(self,color):
        if color == '#FFFFFF':
            return '0'
        if color == '#0000FF':
            return '1'
        if color == "#FF0000":
            return '2'

    #@-others
#@-others
if __name__ == '__main__':
    bj = '0903101'
    filename = 'kb.html'
    newpage = jwc()
    newpage.set_js('21','一校区')
    tp = jsparser()
    tp.feed(newpage.view_data())
    #tp.getresult()
    s=tp.get_status()
    for key in s:
        print key



#@-leo
