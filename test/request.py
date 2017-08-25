# -*- coding:utf-8 -*-
import requests
url = 'http://www.baidu.com'
html = requests.get(url)
html.encoding = 'utf-8'
print html.text