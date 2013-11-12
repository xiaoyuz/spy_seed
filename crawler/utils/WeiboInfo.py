# -*- coding: utf8 -*-

import sys,os
import urllib
import urllib2
import re
import json
import reSettings
import User
import Comment
import uselessChars
import stringStructures
import couchDBBasicAction

default_encoding = 'utf8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

class WeiboInfo:#url(arg), author(arg), content, text, time, device, usermentioned, topic, fowardnum, zannum, commentsnum
	def __init__(self, url, author = None):####if author is none, we will get author info from weibo url content
		self.url = url
		self.weibo_content = self.get_url_content(url)
		if author == None:
			self.author = self.getAuthorByWeiboContent()
		else:
			self.author = author
		self.text = self.get_Weibo_text()
		tad = self.get_time_and_device()
		self.time = tad[0]
		self.device = tad[1]
		self.usermentioned = self.getUserMentioned()
		self.topic = self.getTopic()
		self.fowardnum = self.getFowardNum()
		self.zannum = self.getZanNum()
		self.commentsnum = self.getCommentsNum()
		self.origin_author = self.getOriginAuthor()
		db = couchDBBasicAction.getDB('wb_' + str(self.author.id))
		couchDBBasicAction.insertDoc(db, 'time_' + self.time + '_' + self.url, self.toJson())

	def getAuthorByWeiboContent(self):
		author = User.User(self.url, self.weibo_content)####here the url is not used in fact
		return author

	def getAuthorByUserId():
		return ''
		
	def get_time_and_device(self):
		content = self.weibo_content
		tdList = re.findall(reSettings.time_device_pat, content)
		if len(tdList) != 0:
			return tdList[0][0], tdList[0][1]
		else :
			return '', ''

	# def get_all_comment_info(self):######################################external
	# 	all_comments = []
	# 	page = 1
	# 	while True:
	# 		comments = self.get_comment_in_page(self.url, page)
	# 		if len(comments) == 0:
	# 			break
	# 		all_comments.extend(comments)
	# 		page = page + 1
	# 	self.comments = all_comments
	# 	return all_comments

	def get_url_content(self, url):
		req = urllib2.Request(url=url,)
		result = urllib2.urlopen(req)
		text = result.read().decode('utf8')	
		return text

	def get_comment_in_page(self, weibo_url, page):
		content = self.get_url_content(weibo_url + '?type=comment&page=' + str(page))
		info_list = re.findall(reSettings.comment_infos_pat, content)
		comments = []
		for x in xrange(0, len(info_list)):
			one_comment = Comment(info_list[x][0], info_list[x][2], text_spliter(info_list[x][1]))
			comments.append(one_comment)
		return comments

	def get_Weibo_text(self):
		weibo_whole_text = ''
		content = self.weibo_content
		textList = re.findall(reSettings.weibo_text_pat, content)
		weibo_text_list = []
		for x in textList:
			weibo_text_list.append(text_spliter(x))

		if len(weibo_text_list) != 0:
			weibo_whole_text = weibo_whole_text + weibo_text_list[0]

		feed_userList = re.findall(reSettings.weibo_text_feed_user_pat, content)
		feed_user = ''
		if len(feed_userList) == 0:
			return weibo_whole_text
		else :
			feed_user = feed_userList[0]

			feed_textList = re.findall(reSettings.weibo_text_feed_text_pat, content)

			weibo_feed_text_list = []
			for x in feed_textList:
				weibo_feed_text_list.append(text_spliter(x))

			weibo_whole_text = weibo_whole_text + ' RT FROM: ' + feed_user + ': ' + weibo_feed_text_list[0]
			return weibo_whole_text

	def getUserMentioned(self):####url and name
		fowardPart = self.getFowardParts()
		atname_list = re.findall(reSettings.atname_pat, fowardPart)
		usermentioned = []
		for x in atname_list:
			usermentionedDict = {}
			usermentionedDict['name'] = str(x)
			usermentionedDict['url'] = stringStructures.name_url_structure + str(x)
			usermentioned.append(usermentionedDict)
		return usermentioned

	def getTopic(self):
		fowardPart = self.getFowardParts()
		topic_list = re.findall(reSettings.topic_pat, fowardPart)
		topic = []
		for x in topic_list:
			topicDict = {}
			topicDict['name'] = str(x)
			topic.append(topicDict)
		return topic

	def getFowardNum(self):
		fowardnum = re.findall(reSettings.foward_num_pat, self.weibo_content)
		try:
			return int(fowardnum[0])
		except Exception, e:
			return 0

	def getZanNum(self):
		zannum = re.findall(reSettings.zan_num_pat, self.weibo_content)
		try:
			return int(zannum[0])
		except Exception, e:
			return 0

	def getCommentsNum(self):
		commentsnum = re.findall(reSettings.comments_num_pat, self.weibo_content)
		try:
			return int(commentsnum[0])
		except Exception, e:
			return 0

	def getOriginAuthor(self):
		originauthor = re.findall(reSettings.origin_author_pat, self.text)
		try:
			return originauthor[0]
		except Exception, e:
			return ''

	def getFowardParts(self):# if not forwart weibo, return all weibo text
		fowardParts = re.split(r'(\\/\\/)|(RT FROM)', self.text)
		return fowardParts[0]

	def get_pure_text(self):
		text = self.text
		pure_text_list = re.split(reSettings.weibo_pure_text_split_patten, text.encode('utf8'))
		
		pure_text = ''
		for x in xrange(1, len(pure_text_list)):
			pure_text = pure_text + pure_text_list[x] + ' '
		return pure_text

	def toJson(self):
		jsonDict = {}
		jsonDict['url'] = self.url
		jsonDict['author'] = self.author.toJson()
		jsonDict['text'] = self.text
		jsonDict['time'] = self.time
		jsonDict['device'] = self.device
		jsonDict['usermentioned'] = self.usermentioned
		jsonDict['topic'] = self.topic
		jsonDict['fowardnum'] = self.fowardnum
		jsonDict['zannum'] = self.zannum
		jsonDict['commentsnum'] = self.commentsnum
		jsonDict['originauthor'] = self.origin_author
		return jsonDict


# class Comment:
# 	def __init__(self, author, time, text):
# 		self.author = author
# 		self.time = time
# 		self.text = text
# 		self.pure_text = self.get_pure_text()

# 	def get_pure_text(self):
# 		text = self.text
# 		pure_text_list = re.split(reSettings.comment_pure_text_split_patten, text.encode('utf8'))
		
# 		pure_text = ''
# 		for x in xrange(1, len(pure_text_list)):
# 			pure_text = pure_text + pure_text_list[x] + ' '
# 		return pure_text

def text_spliter(text):
	split_list = re.split(r'<.*?>', text)
	splited_text = ''
	for item in split_list:
		if item != '' and item != ' ' and item != '\\n\\t\\t\\t' and item != '\\n\\t\\t' and item != '\\t\\t\\t':
			splited_text = splited_text + item + ' '
	return splited_text
