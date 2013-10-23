# -*- coding: utf8 -*-

import sys,os
import urllib
import urllib2
import re
import json
import reSettings
import stringStructures

class Comment:
	def __init__(self, authorid, authorname, weibo_url, time, text):
		self.authorid = authorid
		self.authorname = authorname
		self.time = time
		self.weibo_url = weibo_url
		self.text = text
		self.usermentioned = self.getUsermentioned()
		self.topic = self.getTopic()
		self.pure_text = self.get_pure_text()

	def getUsermentioned(self):
		atname_list = re.findall(reSettings.atname_pat, self.text)
		usermentioned = []
		for x in atname_list:
			usermentionedDict = {}
			usermentionedDict['name'] = str(x)
			usermentionedDict['url'] = stringStructures.name_url_structure + str(x)
			usermentioned.append(usermentionedDict)
		return usermentioned

	def getTopic(self):
		topic_list = re.findall(reSettings.topic_pat, self.text)
		topic = []
		for x in topic_list:
			topicDict = {}
			topicDict['name'] = str(x)
			topic.append(topicDict)
		return topic

	def get_pure_text(self):# without @ or ## etc.
		text = self.text
		pure_text_list = re.split(reSettings.comment_pure_text_split_patten, text.encode('utf8'))
		
		pure_text = ''
		for x in xrange(1, len(pure_text_list)):
			pure_text = pure_text + pure_text_list[x] + ' '
		return pure_text

	def toJson(self):
		jsonDict = {}
		author = {}
		author['id'] = self.authorid
		author['name'] = self.authorname
		jsonDict['author'] = author
		jsonDict['weibo_url'] = self.weibo_url
		jsonDict['time'] = self.time
		jsonDict['text'] = self.text
		jsonDict['usermentioned'] = self.usermentioned
		jsonDict['topic'] = self.topic
		return jsonDict


def getCommentsByWeiboUrl(weibo_url, startPage = None, endPage = None):
	page = 1
	if startPage != None:
		page = startPage
	if endPage == None:
		endPage = sys.maxint
	comment_list = []
	while page <= endPage:
		comments = get_comment_in_page(weibo_url, page)
		if len(comments) == 0:
			break
		else:
			comment_list.extend(comments)
			page = page + 1
	return comment_list

def get_comment_in_page(weibo_url, page):
	print weibo_url + '?type=comment&page=' + str(page)
	content = get_url_content(weibo_url + '?type=comment&page=' + str(page))
	info_list = re.findall(reSettings.comment_infos_pat, content)
	comments = []
	for x in xrange(0, len(info_list)):
		text = info_list[x][2].split('<\\/a>：')[1]
		text = text_spliter(text)
		one_comment = Comment(info_list[x][1], info_list[x][0], weibo_url, info_list[x][3], text)
		
		comments.append(one_comment)
	return comments
		

def text_spliter(text):
	split_list = re.split(r'<.*?>', text)
	splited_text = ''
	for item in split_list:
		if item != '' and item != ' ' and item != '\\n\\t\\t\\t' and item != '\\n\\t\\t' and item != '\\t\\t\\t':
			splited_text = splited_text + item + ' '
	return splited_text

def get_url_content(url):
	req = urllib2.Request(url=url,)
	result = urllib2.urlopen(req)
	text = result.read().decode('utf8')	
	return text