# -*- coding: utf8 -*-

import urllib
import urllib2
import re
import json

class FriendInfo:
	def __init__(self, id, name, sex):
		self.id = id
		self.name = name
		self.sex = sex
		