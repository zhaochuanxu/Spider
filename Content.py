import requests
import urllib.request

  #rps = requests.get("")

response = urllib.request.urlopen('http://cscy.lib.whu.edu.cn/preRequest2.html')
html =str(response.read(),'utf-8')
with open('b.txt','w',encoding='utf-8') as f:
    f.write((html))
print(html)




