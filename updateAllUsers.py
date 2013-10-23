# -*- coding: utf8 -*-
import importSettings
import sys
import operator
from login import spylogin
from crawler import spy_in_onepage
from crawler import spy_in_followers_list
from crawler.utils import User
import urllib2
import redisUserAction
import stringStructures

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

def updateAll():
	index = 0
	while True:
		id = redisUserAction.getIdByListIndex(index)
		if id == None:
			break;
		updateUser(id)
		index = index + 1

def updateUser(id):
	user = User.User(stringStructures.id_url_structure + str(id))
	user.updateInfo()

updateAll()