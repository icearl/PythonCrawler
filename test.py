import urllib
import urllib2
import re


page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile(
        r'h2>(.*?)</h2.*?<span>(.*?)</span>.*?</div(.*?)number">(.*?)</i.*?number">(.*?)</', re.S)
    # print 'nice'
    items = re.findall(pattern,content)
    for item in items:
        # print 'loop'
        haveImg = re.search("img",item[2])
        if not haveImg:
            print item[0],item[1],item[3],item[4]
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

