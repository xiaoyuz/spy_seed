# -*- coding: utf8 -*-

import redisBasicAction

def importUser(user):
	#id index
	redisBasicAction.set('user$id:' + user.id + ':url', user.url)
	redisBasicAction.set('user$id:' + user.id + ':nurl', user.nurl)
	redisBasicAction.set('user$id:' + user.id + ':name', user.name)
	redisBasicAction.set('user$id:' + user.id + ':sex', user.sex)
	redisBasicAction.set('user$id:' + user.id + ':description', user.description)
	redisBasicAction.set('user$id:' + user.id + ':location', user.location)
	#name index
	redisBasicAction.set('user$name:' + user.name + ':id', user.id)
	#url index
	redisBasicAction.set('user$url:' + user.url + ':id', user.id)
	#nurl index
	redisBasicAction.set('user$nurl:' + user.nurl + ':id', user.id)
	#sex set
	redisBasicAction.setAdd('user$sexset:' + user.sex + ':id', user.id)

def dropUser(user):
	#id index
	redisBasicAction.delete('user$id:' + user.id + ':url')
	redisBasicAction.delete('user$id:' + user.id + ':nurl')
	redisBasicAction.delete('user$id:' + user.id + ':name')
	redisBasicAction.delete('user$id:' + user.id + ':sex')
	redisBasicAction.delete('user$id:' + user.id + ':description')
	redisBasicAction.delete('user$id:' + user.id + ':location')
	#name index
	redisBasicAction.delete('user$name:' + user.name + ':id')
	#url index
	redisBasicAction.delete('user$url:' + user.url + ':id')
	#nurl index
	redisBasicAction.delete('user$nurl:' + user.nurl + ':id')
	#sex set
	redisBasicAction.setRemove('user$sexset:' + user.sex + ':id', user.id)

def getUrlById(id):
	return redisBasicAction.get('user$id:' + id + ':url')
def getNUrlById(id):
	return redisBasicAction.get('user$id:' + id + ':nurl')
def getNameById(id):
	return redisBasicAction.get('user$id:' + id + ':name')
def getSexById(id):
	return redisBasicAction.get('user$id:' + id + ':sex')
def getDescriptionById(id):
	return redisBasicAction.get('user$id:' + id + ':description')
def getLocationById(id):
	return redisBasicAction.get('user$id:' + id + ':location')

def getIdByName(name):
	return redisBasicAction.get('user$name:' + name + ':id')
def getIdByUrl(url):
	if redisBasicAction.get('user$url:' + url + ':id') != None:
		return redisBasicAction.get('user$url:' + url + ':id')
	elif redisBasicAction.get('user$nurl:' + url + ':id') != None:
		return redisBasicAction.get('user$nurl:' + url + ':id')
	else:
		return None
