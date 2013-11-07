# -*- coding: utf8 -*-
import importSettings
import sys
import operator
import jieba
import jieba.analyse
import nltk
from login import spylogin
from crawler import spy_in_onepage
from crawler import spy_in_followers_list
from crawler.utils import WeiboInfo
from crawler.utils import User
import urllib2
import Comment

default_encoding = 'utf8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

spylogin.login()
# jt: 1760242980
# kaifu: 1197161814
# me:2109690092
# zc:1845299841
# xt: 3503035751
# lt: 2327875205
# zyy: 2040278193
# hxy: 1324608471
# keshuidexiaotuzi: 1883514540
# 'http://weibo.com/1197161814/A6X8fDt4y'

def get_url_content(url):
	req = urllib2.Request(url=url,)
	result = urllib2.urlopen(req)
	text = result.read().decode('utf8')	
	return text

user = User.User('http://weibo.com/u/2109690092')
# print user.toJson()
weiboUrls = spy_in_onepage.get_weibo_urls(user)
for url in weiboUrls:
	print url
	print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
	weiboinfo = WeiboInfo.WeiboInfo(url)


# weiboinfo = WeiboInfo.WeiboInfo(weiboUrls[0])
# print weiboinfo.toJson()
# commentList = Comment.getCommentsByWeiboUrl(weiboUrls[0])
# print commentList[0].toJson()['time']