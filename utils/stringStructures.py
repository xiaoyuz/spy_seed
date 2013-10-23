# -*- coding: utf8 -*-

import sys

default_encoding = 'utf8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

id_url_structure = 'http://weibo.com/u/'

name_url_structure = 'http://weibo.com/n/'