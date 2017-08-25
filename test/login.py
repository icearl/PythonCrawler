import urllib
import urllib2

# values = {"username": "ice_now@163.com", "password": "124578"}
# data = urllib.urlencode(values)
# url = "https://www.zhihu.com/#signin"
# request = urllib2.Request(url, data)
# response = urllib2.urlopen(request)
# print response.read()

# values = {"username": "306030928@qq.com", "password": "124578"}
# data = urllib.urlencode(values)
# url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib2.Request(url, data)
# response = urllib2.urlopen(request)
# print response.read()


values={}
values['username'] = "306030928@qq.com"
values['password']="124578"
data = urllib.urlencode(values)
url = "https://www.zhihu.com/#signin"
geturl = url + "?"+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()