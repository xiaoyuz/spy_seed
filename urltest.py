import urllib2


request = urllib2.Request('http://localhost:8080/rest-resteay-demo/delete/1')
request.get_method = lambda : 'DELETE'

response = urllib2.urlopen(request)
print response.info()