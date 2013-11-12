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
from crawler.utils import Comment
from crawler.utils import User
import urllib2

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

users = {}
user = User.User('http://weibo.com/u/1883514540')
# print user.toJson()
weiboUrls = spy_in_onepage.get_weibo_urls(user,1, 5)
for url in weiboUrls:
	comments = Comment.getCommentsByWeiboUrl(url)
	for x in comments:
		print x.authorname
		if x.authorname in users:
			users[x.authorname] = users[x.authorname] + 1
		else:
			users[x.authorname] = 1

hotuserkv = sorted([(v, k) for k, v in users.items()], reverse=True)
hotuserinfos = ''
for userkv in hotuserkv:
	try:
		user = User.User('http://weibo.com/n/' + userkv[1])
		hotuserinfos = hotuserinfos + user.toString() + '	' + str(userkv[0]) + '\n'
	except Exception, e:
		continue
# result = ''
# for x in hotuserkv:
# 	result = result + x[1] + '	' + str(x[0]) + '\n'
print hotuserinfos
try:
	with open('hotusers', "w") as data:
		data.write(hotuserinfos)
except Exception, e:
	raise e