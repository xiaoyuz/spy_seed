# -*- coding: utf8 -*-

import urllib
import urllib2
import re
import json

def get_url_content(url):
	req = urllib2.Request(url=url,)
	result = urllib2.urlopen(req)
	text = result.read().decode('utf8')	
	return text