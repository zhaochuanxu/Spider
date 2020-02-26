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

yeast = pd.read_excel("./data.xlsx")
#   print(yeast)

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
    with open("Content.txt",'r',encoding='utf-8') as f:
        s = f.read()
    #print(s)

    soup = BeautifulSoup(s,'html.parser')


        #然后使用soup的属性
    soup.name = soup.find_all(name='a',attrs={"class":"textIntent-headline1 agentCard-name"})
    soup.Email = soup.find_all(name='a',attrs={"class":"textIntent-body agentCard-email"})
    soup.phone = soup.find_all(name='a',attrs={"class":"textIntent-body agentCard-phone"})
    num = len(soup.Email)

    #print(soup.Email[0].string)
   # print(len(soup.a))

    #for i in range(0,len(soup.a)): ##循环写入
        #print(soup.a[i].string.strip())
        #print("\n")
    #print(data)



    count = 0
    with open("./data.csv", 'a',newline='') as f:#a表示在文末追加，newline用于去除间隔的空行
        writer = csv.writer(f)
        writer.writerow(["姓名", "邮箱", "电话"])  # 先写入列名
        for i in range(0,num):
            writer.writerows([[soup.name[i].string,soup.Email[i].string,soup.phone[i].string]])# 写入多行用writerows，一次在一行写入三个数值









if __name__ == "__main__":
    #Get_url("https://www.compass.com/agents/boston/")
    Get_info()