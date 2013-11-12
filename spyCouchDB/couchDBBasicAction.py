# -*- coding: utf8 -*-

import couchdb

couch = couchdb.Server('http://127.0.0.1:5984/')

def getDB(db_name):
	db = None
	try:
		db = couch.create(db_name)
	except Exception, e:
		db = couch[db_name]
	return db

def insertDoc(db, key, doc_json):
	try:
		db[key] = doc_json
	except Exception, e:
		pass
	

def deleteDocByKey(db, key):
	try:
		doc = db[key]
		db.delete(doc)
	except Exception, e:
		pass
	

def updateDocByKey(db, key, doc_json):
	deleteDocByKey(db, key)
	insertDoc(db, key, doc_json)

db = getDB('test')
insertDoc(db, 'ins', {'ddd': 'ccc'})