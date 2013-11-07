# -*- coding: utf8 -*-
import json
import couchdb

couch = couchdb.Server()

db = couch['test']
db.update(json.loads("{'aa': 'bb'}"), all_or_nothing = True)