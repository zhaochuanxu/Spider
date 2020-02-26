import os
import bs4
import requests
import re
from bs4 import BeautifulSoup
import  time
import hashlib
import pandas as pd
import re
import openpyxl

import csv
#t提取所有的

def Get_url(url):
   rps = requests.get(url)
   state = str(rps)
   print(state)
   r =re.search(r'200',state) #【】是列表
    #print(r)
    #print(r.group())
       # #print("匹配到了"
   if r==None:  #这时候没有提取到
      print("网络状态错误")
   else:
        #提取到了 用group进行取出
       print("网络状态正常")
       #print(url[len(url)-1])
       name = "./elliman/elliman_"+url[len(url)-1]+".txt"
       with open(name,'w',encoding='utf-8') as f:
          f.write(rps.text)
       print(name+"写入成功")
       Catch_url(url[len(url)-1])


def Catch_url(N):
   name  =  name = "./elliman/elliman_"+N+".txt"
   with open(name,'r',encoding='utf-8') as f:
      s = f.read()
   print()






if __name__ == "__main__":
    #Get_url("https://www.elliman.com/agents/massachusetts/")
   for i in range(ord("z"),ord("z")):
       #print(chr(i))  //循环遍历i
      url = "https://www.elliman.com/agents/massachusetts/"+chr(i)
      #print(url)

      #et_url(url)
    Get_url("https://www.elliman.com/agents/massachusetts/z")