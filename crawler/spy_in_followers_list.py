# -*- coding: utf8 -*-

import urllib
import urllib2
import re
import json
import common
from utils import Friend
import weibo
import weiboAuthSetting



def get_follower_infos(id):
	followerListUrl = 'http://weibo.com/p/100505' + str(id) + '/follow?relate=fans&page='
	followerList = []
	page = 1
	while True:
		url = followerListUrl + str(page)
		page = page + 1
		content = common.get_url_content(url)
		friend_list_pat = re.compile(r'<li class=\\\"clearfix S_line1\\\".*?uid=(.*?)&fnick=(.*?)&sex=(.*?)\\\">')
		follower_list_list = re.findall(friend_list_pat, content)
		if len(follower_list_list) == 0:
			break
		for x in follower_list_list:
			followerList.append(Friend.FriendInfo(x[0], x[1], x[2]))
	return followerList

def get_followed_infos(id):
	next_coursor = 0
	followedListUrl = 'https://api.weibo.com/2/friendships/friends.json?uid=' + str(id) + '&cursor=' + next_coursor + '&access_token=2.00YlCmSCMYmPKE8da11d9359t_17GE'
	followedList = []
	page = 1
	while True:
		url = followedListUrl + str(page)
		print page
		page = page + 1
		print url
		content = common.get_url_content(url)
		friend_list_pat = re.compile(r'<li class=\\\"clearfix S_line1\\\".*?uid=(.*?)&fnick=(.*?)&sex=(.*?)\\\">')
		followed_list_list = re.findall(friend_list_pat, content)
		if len(followed_list_list) == 0:
			break
		print url
		for x in followed_list_list:
			followedList.append(Friend.FriendInfo(x[0], x[1], x[2]))
	return followedList


#http://weibo.com/p/1005051760242980/follow?relate=fans&page=2#place
def test():
	# listt = get_followed_infos(1760242980)
	# for x in listt:
	# 	print x.id + '	' + x.name + '	' + x.sex
	# print len(listt)

	# followedListUrl = 'https://api.weibo.com/2/friendships/friends.json?uid=' + str(1760242980) + '&cursor=' + '0' + '&access_token=2.00YlCmSCMYmPKE8da11d9359t_17GE'
	# print followedListUrl
	# content = common.get_url_content(followedListUrl)
	# print content

	client = weibo.APIClient(app_key=weiboAuthSetting.app_key, app_secret=weiboAuthSetting.app_secret, redirect_uri=weiboAuthSetting.callback_url)
	#新浪返回的token，类似abc123xyz456，每天的token不一样
	url = client.get_authorize_url()
	print url
	code = your.web.framework.request.get('code')
	r = client.request_access_token(code)
	access_token = r.access_token
	expires_in = r.expires_in # token过期的UNIX时间

	#设置得到的access_token
	client.set_access_token(access_token, expires_in)

	#有了access_token后，可以做任何事情了
	print client.get.friendships__followers()
	
