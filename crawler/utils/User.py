# -*- coding: utf8 -*-

import sys,os
import urllib
import urllib2
import re
import json
import reSettings
import stringStructures
import uselessChars
import redisUserAction

default_encoding = 'utf8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

class User:
	def __init__(self, url, content = None):####if content is not none, url may not be the author url, it need to be changed
		if content != None:
			self.content = content
			self.setParamsWithContent()
		else:
			self.url = url###here we don not know it is url or nurl
			rid = redisUserAction.getIdByUrl(self.url)
			if rid == None:
				self.content = self.get_url_content(self.url)
				self.setParamsWithContent()
				redisUserAction.importUser(self)
			else:
				self.id = rid
				self.url = redisUserAction.getUrlById(self.id)
				self.name = redisUserAction.getNameById(self.id)
				self.nurl = redisUserAction.getNUrlById(self.id)
				self.sex = redisUserAction.getSexById(self.id)
				self.description = redisUserAction.getDescriptionById(self.id)
				self.location = redisUserAction.getLocationById(self.id)

	def updateInfo(self):
		redisUserAction.dropUser(self)
		self.content = self.get_url_content(self.url)
		self.setParamsWithContent()
		redisUserAction.importUser(self)

	def setParamsWithContent(self):
		self.id = self.getId()
		self.url = self.getUrl()####url should like 'weibo.com/u/${id}'
		self.name = self.getName()
		self.nurl = self.getNUrl()###url that built by name
		self.sex = self.getSex()
		self.description = self.getDescription()
		self.location = self.getLocation()

	def getId(self):
		id = re.findall(reSettings.user_id_pat, self.content)
		try:
			return str(id[0])
		except Exception, e:
			return ''

	def getUrl(self):
		return stringStructures.id_url_structure + str(self.id)

	def getNUrl(self):
		return stringStructures.name_url_structure + str(self.name)

	def getName(self):
		name = re.findall(reSettings.user_name_pat, self.content)
		try:
			return str(name[0])
		except Exception, e:
			return ''

	def getSex(self):
		sex = re.findall(reSettings.user_sex_pat, self.content)
		try:
			return str(sex[0])
		except Exception, e:
			return ''

	def getDescription(self):
		description = re.findall(reSettings.user_desc_pat, self.content)
		try:
			return str(description[0])
		except Exception, e:
			return ''

	def getLocation(self):
		location = re.findall(reSettings.user_loc_pat, self.content)
		try:
			return str(location[0])
		except Exception, e:
			return ''

	def get_url_content(self, url):
		req = urllib2.Request(url=url,)
		print '========================================='
		print url
		result = urllib2.urlopen(req)
		text = result.read()	
		return text

	def toJson(self):
		jsonDict = {}
		jsonDict['id'] = self.id
		jsonDict['url'] = self.url
		jsonDict['name'] = self.name
		jsonDict['sex'] = self.sex
		jsonDict['description'] = self.description
		jsonDict['location'] = self.location
		return jsonDict

	def toString(self):
		return 'name:' + self.name + '	' + 'id:' + self.id + '	' + 'sex:' + self.sex + '	' + 'description:' + self.description + '	' + 'location:' + self.location



