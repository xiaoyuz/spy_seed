# -*- coding: utf8 -*-

import sys
import re

default_encoding = 'utf8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

time_device_pat = re.compile(r'class=\\\"S_link2 WB_time\\\" title=\\\"(.*?)\\\".*?<em class=\\\"S_txt2\\\">.*?<\\\/em><a class=\\\"S_link2\\\".*?>(.*?)<\\\/a>')

comment_infos_pat = re.compile(r'<dl class=\\\"comment_list S_line1\\\".*?<dt>.*?<a href=.*?title=\\\"(.*?)\\\">.*?usercard=\\\"id=(.*?)\\\"(.*?)<span class=.*?S_txt2.*?>\((.*?)\)<.*?span>')

weibo_text_pat = re.compile(r'<div class=.*?WB_text.*?>\\n    <p>\\n                <em nick-name=.*?>(.*?)\\n            <\\\/p>\\n<\\\/div>')

weibo_text_feed_user_pat = re.compile(r'<a class=\\\"WB_name S_func3\\\".*?>(.*?)<\\\/a>')

weibo_text_feed_text_pat = re.compile(r'<div class=\\\"WB_text\\\">(.*?)<\\\/div>')

weibo_url_pat = re.compile(r'allowForward=1.*?&url=(.*?)&mid')

user_name_pat = re.compile(r'<span class=\\\"name\\\">(.*?)<')

user_sex_pat = re.compile(r'loc=infgender\\\"><em class=\\\"W_ico12 (.*?)\\\" title=.*?>')

user_desc_pat = re.compile(r'pf_intro bsp\\\">.*?<span class=\\\"S_txt2\\\" title=\\\"(.*?)\\\">')

user_loc_pat = re.compile(r'loc=infsign\\\" title=\\\"(.*?)\\\">')

user_id_pat = re.compile(r'CONFIG.?\'oid\'.?=\'(.*?)\';')

foward_num_pat = re.compile(r'<a node-type=\\\"forward_counter\\\" href=\\\"javascript:void.?0.?;\\\">.?.?.?(.*?).?<\\/a><em class=\\\"S_txt3\\\">')

zan_num_pat = re.compile(r'<a href=\\\"javascript:void.?0.?;\\\" action-data=\\\"like_src=1\\\" node-type=\\\"like_counter\\\" title=\\\".?\\\"><em class=\\\"W_ico20 icon_praised_b\\\"><\\/em>.?(.*?).?<\\/a><i class=\\\"S_txt3\\\">')

comments_num_pat = re.compile(r'<a href=\\\"javascript:void.?0.?;\\\" node-type=\\\"comment_counter\\\">.?.?.?(.*?).?<\\/a>')

atname_pat = re.compile(r'@(.*?) ')

topic_pat = re.compile(r'#(.*?)#')

origin_author_pat = re.compile(r'RT FROM: @(.*?):')

weibo_pure_text_split_patten = r':|：|回复|@.*? |RT FROM|#.*?#|我在这里: \| .*? |我在: \| .*? | \| .*? |分享'

comment_pure_text_split_patten = r':|：|回复|@.*? '


