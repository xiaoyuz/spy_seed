# -*- coding: utf8 -*-

import sys

default_encoding = 'utf8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

web_content_splits = [' ', '\\n\\t\\t\\t' ,'\\n\\t\\t', '\\t\\t\\t']
