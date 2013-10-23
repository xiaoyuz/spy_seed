#!/usr/bin/env python
#coding=utf-8
'''
Created on 2011-12-5

@author: chenjian
'''
import sys,time
import urllib2,urllib
import cookielib
from datetime import date

class Publish(object):
    
    def __init__(self):
        self.operate = ''
        self.cj = cookielib.LWPCookieJar()
        try:  
            self.cj.revert('ab.coockie')  
        except Exception,e:
            print e
            
        self.opener =urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj)) 
        urllib2.install_opener(self.opener)
    
    def publishFolders(self):
        url = 'http://rp.oupeng.com:8083/domain/init/redis/site/folder/1'
        
        login_url = 'http://rp.oupeng.com:8083/resources/j_spring_security_check'
        data = urllib.urlencode({'j_username':'chenjian','j_password':'chenjian'})
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        print 'login.......'
        req = urllib2.Request(login_url,data,headers)
        self.operate = self.opener.open(req)
        self.cj.save('rp.coockie')
        print 'login success.......'
        print 'publish site folders .......'
        req = urllib2.Request(url,urllib.urlencode({}),headers)
        self.operate = self.opener.open(req)
        print 'publish success .......'

def productsbyday():
    url = 'http://59.151.111.95:8080/task/publish/recommand/productsbyday'
    try:
        r1 = urllib2.urlopen(url, None, 1)
    except Exception as ex:
        print 'ok'
        
def freefolder():
    folder_map = {
                  57:302,
                  58:303,
                  59:304,
                  60:305,
                  61:306,
                  62:307,
                  63:308,
                  64:309,
                  65:310,
                  66:311,
                  67:312,
                  68:313,
                  69:314,
                  70:315,
                  141:316
                  }
    
    for key in folder_map.keys():
        value = folder_map.get(key)
        url = 'http://59.151.111.95:8080/task/publish/free/' + str(key) + '/' + str(value)
        try:
            print url
            r1 = urllib2.urlopen(url, None, 1)
        except Exception as ex:
            print 'ok'
        time.sleep(10)
        
def currentmonthfinished():
    url = 'http://59.151.111.95:8080/task/publish/currentmonthfinished/1/' + str(date.today())
    try:
        print url
        r1 = urllib2.urlopen(url, None, 1)
    except Exception as ex:
        print 'ok'
    pass

def removeoutdatedrecommand():
    url = 'http://59.151.111.95:8080/task/publish/removeoutdatedrecommand'
    try:
        print url
        r1 = urllib2.urlopen(url, None, 1)
    except Exception as ex:
        print 'ok'
    pass
    
if __name__ == '__main__':
    # if len(sys.argv) >= 2:
    #     job_type = sys.argv[1]
    #     if job_type == 'folders':
    #         p = Publish()
    #         p.publishFolders()
    #     elif job_type == 'productsbyday':
    #         productsbyday()
    #     elif job_type == 'freefolder':
    #         freefolder()
    #     elif job_type == 'currentmonthfinished':
    #         currentmonthfinished()
    #     elif job_type == 'removeoutdatedrecommand':
    #         removeoutdatedrecommand()
    # else:
    #     p = Publish()
    #     p.publishFolders()
    currentmonthfinished()

