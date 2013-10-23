# -*- coding: utf8 -*-

import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)


# def getConnection():
# 	r = redis.Redis(connection_pool=pool)
# 	return r

def set(key, value):
	return r.set(key, value)

def get(key):
	return r.get(key)

def delete(key):
	return r.delete(key)

# def listPush(list_name, value):
# 	r = getConnection()
# 	return r.rpush(list_name, value)

# def listGet(list_name, index):
# 	r = getConnection()
# 	return r.lindex(list_name, index)

# def listRemove(list_name, value):
# 	r = getConnection()
# 	return r.lrem(list_name, 0, value)
def setAdd(set_name, value):
	return r.sadd(set_name, value)

def setRemove(set_name, value):
	return r.srem(set_name, value)

def setIsMember(set_name, value):
	return r.sismember(set_name, value)

print r.keys('us')


# print setAdd('message', '1')
# print setRemove('message', '3')
# print listRemove('message', '1')
# print listGet('message', 0)
# print setIsMember('message', '3')

# r.set('foo', 'bar')
# print r.get('foo')
# print r.get('user$id:2109690092:nurl')