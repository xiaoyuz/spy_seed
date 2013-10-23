# -*- coding: utf8 -*-

import urllib
import urllib2
import cookielib
import base64
import re
import json
import hashlib
import rsa
import binascii
import setting
import sys

default_encoding = 'utf8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


#获取一个保存cookie的对象
cj = cookielib.LWPCookieJar()
#将一个保存cookie对象，和一个HTTP的cookie的处理器绑定
cookie_support = urllib2.HTTPCookieProcessor(cj)
#创建一个opener，将保存了cookie的http处理器，还有设置一个handler用于处理http的URL的打开
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
#将包含了cookie、http处理器、http的handler的资源和urllib2对象板顶在一起
urllib2.install_opener(opener)

def get_servertime():
    data = urllib2.urlopen(setting.prelogin_url).read()
    p = re.compile('\((.*)\)')
    try:
        json_data = p.search(data).group(1)
        data = json.loads(json_data)
        servertime = str(data['servertime'])
        nonce = data['nonce']
        pubkey = data['pubkey']
        rsakv = data['rsakv']
        return servertime, nonce, pubkey, rsakv
    except:
        print 'Get severtime error!'
        return None

def get_pwd(pwd, servertime, nonce, pubkey):
    rsaPublickey = int(pubkey, 16)
    key = rsa.PublicKey(rsaPublickey, 65537) #创建公钥
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(pwd) #拼接明文js加密文件中得到
    passwd = rsa.encrypt(message, key) #加密
    passwd = binascii.b2a_hex(passwd) #将加密信息转换为16进制。
    return passwd

def get_user(username):
    username_ = urllib.quote(username)
    username = base64.encodestring(username_)[:-1]
    return username

def get_url_content(url):
    #测试读取数据，下面的URL，可以换成任意的地址，都能把内容读取下来
	req = urllib2.Request(url=url,)
	result = urllib2.urlopen(req)
	text = result.read().decode('utf8')	
	return text

def is_logininfo_correct():
	req  = urllib2.Request(
        url = setting.spy_login_url,
        data = setting.postdata,
        headers = setting.headers
    )
	result = urllib2.urlopen(req)
	text = result.read()
	p = re.compile('location\.replace\(\"(.*?)\"\)')
	try:
		login_url = p.search(text).group(1)
		print login_url
		login_info_text = urllib2.urlopen(login_url)
		p = re.compile('\((.*)\)')
		json_data = p.search(login_info_text.read()).group(1)
		info = json.loads(json_data)
		print info
		if info['result'] is True:
			print "Login success! Login user: " + info['userinfo']['displayname']
			return True
		else:
			print "Login infomation is not correct! Errno: " + info['errno']
			return False
		#print "login success"
	except:
		print 'Login error!'
		return False

def login():
  	try:
		servertime, nonce, pubkey, rsakv = get_servertime()
	except:
		return
	#global setting.postdata
	print servertime
	setting.postdata['servertime'] = servertime
	setting.postdata['nonce'] = nonce
	setting.postdata['su'] = get_user(setting.username)
	setting.postdata['sp'] = get_pwd(setting.pwd, servertime, nonce, pubkey)
	setting.postdata['rsakv'] = rsakv
	setting.postdata = urllib.urlencode(setting.postdata)
	login_suc = is_logininfo_correct()
    #其实到了这里，已经能够使用urllib2请求新浪任何的内容了，这里已经登陆成功了
	# if login_suc:
		#text = get_url_content('http://weibo.com/2109690092/profile')
		#print eval("u'''"+text+"'''")	
		# print get_url_content('http://weibo.com/p/aj/mblog/mbloglist?pre_page=1&page=1&id=1005052109690092&pagebar=0')

# login()