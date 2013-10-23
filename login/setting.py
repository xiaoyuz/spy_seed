# -*- coding: utf8 -*-

prelogin_url = 'http://login.sina.com.cn/sso/prelogin.php?entry=sso&callback=sinaSSOController.preloginCallBack&su=%s&rsakt=mod&client=ssologin.js(v1.4.4)'
spy_login_url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.4)'

postdata = {
        'entry': 'weibo',
        'gateway': '1',
        'from': '',
        'savestate': '7',
        'userticket': '1',
        'ssosimplelogin': '1',
        'vsnf': '1',
        'vsnval': '',
        'su': '',
        'service': 'miniblog',
        'servertime': '',
        'nonce': '',
        'pwencode': 'rsa2',
        'sp': '',
        'encoding': 'UTF-8',
        'prelt': '115',
        'rsakv' : '',
        'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype': 'META'
    }

username = '13121260694'
# username = 'alexanderxiaoyu@163.com'
pwd = '2858300wcc'
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0'}