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


from openpyxl import load_workbook

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
       with open('Content.txt','w',encoding='utf-8') as f:
            f.write(rps.text)


def Get_info():
   name =
   with open(name,'r',encoding='utf-8') as f:
      s = f.read()
   #print(s)


   soup = BeautifulSoup(s,'html.parser')


        #然后使用soup的属性
  # soup.all = soup.find_all(name="tbody")
   #soup.name = soup.find_all(name='td',attrs={"class":"first"})

   soup.Email = soup.find_all(name='td',attrs={"class":"last"})#获取邮箱


def Get_name_info():







if __name__ =="__main__":
    Get_url("https://www.gibsonsothebysrealty.com/agents")