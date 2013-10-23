# -*- coding: utf8 -*-

import sys
import urllib
import urllib2
import re
import json
import common
import reSettings

def get_page_paras(page, bar):
	if bar == 1:
		return page-1, page, 0
	elif bar == 2:
		return page, page, 0
	else:
		return page, page, 1

def get_weibo_urls_in_pagebar(page, bar, id):
	pre_page, page, pagebar = get_page_paras(page, bar)
	#http://weibo.com/u/1760242980
	pagebar_url = 'http://weibo.com/p/aj/mblog/mbloglist?pre_page=' + str(pre_page) + '&page=' + str(page) + '&id=100505' + str(id) + '&pagebar=' + str(pagebar)
	print pagebar_url
	content = common.get_url_content(pagebar_url)
	urlList =re.findall(reSettings.weibo_url_pat, content)
	urlList = [(url.replace('\\', '')) for url in urlList]
	#print len(urlList)
	return urlList

def get_weibo_urls(user, startPage = None, endPage = None): #all weibos if no start and end para
	weibo_urls = []
	page = 1
	if startPage != None:
		page = startPage
	if endPage == None:
		endPage = sys.maxint
	while page <= endPage:
		urls = get_weibo_urls_in_pagebar(page, 1, user.id)
		if len(urls) == 0:
			break
		weibo_urls.extend(urls)
		urls = get_weibo_urls_in_pagebar(page, 2, user.id)
		if len(urls) == 0:
			break
		weibo_urls.extend(urls)
		urls = get_weibo_urls_in_pagebar(page, 3, user.id)
		if len(urls) == 0:
			break
		weibo_urls.extend(urls)
		page = page + 1
	return weibo_urls