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

def Get_url(url,i):   #缓存到本地
   page = str(i)
   url = str(url+page)
   print(url)
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
       filename ="./gibson/"+page+".txt"
       print("正在写入"+page)
       with open(filename,'w',encoding='utf-8') as f:
            f.write(rps.text)
       print("写入"+page+"完成")


def Get_info(i):  #解析网页



    page =str(i)
    with open("./data_2.csv", 'a',newline='') as f:#a表示在文末追加，newline用于去除间隔的空行
        writer = csv.writer(f)
        Page_name="Page"+page
        writer.writerow([Page_name, "",""])  # 先写入列名

    filename ="./gibson/"+page+".txt"
    with open(filename,'r',encoding='utf-8') as f:
      s = f.read()
   #print( s


    soup = BeautifulSoup(s,'html.parser')
    soup.name = soup.find_all(name='div',attrs={"class":"font-hairline text-2xl font-serif"})#获取姓名
    #print(soup.name[5].get_text().replace('\n', '').replace('\r', '').strip())
    for i in range(0,len(soup.name)):
        url = "https://www.gibsonsothebysrealty.com/agents/"+soup.name[i].get_text().replace('\n', '').replace('\r', '').strip()

        print(url)

        rps = requests.get(url)
        n =rps.text
        soup_people = BeautifulSoup(n,'html.parser')
        state = str(rps)
        r =re.search(r'200',state) #【】是列表
    #print(r)
    #print(r.group())
       # #print("匹配到了"
        if r==None:  #这时候没有提取到
            print("网络状态错误")
        else:
            #提取到了 用group进行取出
            print("网络状态正常")


        soup_phone = soup_people.find_all(name='div',attrs={"flex-shrink-0 mr-10"})#获取电话
    #获取每个人含有两个div 的 某个div

    #出来一个 但是里边有两个div
    #print(soup_phone[1])



    # print(Finall_phone_1[0].get("href"))

    # 读取里边两个div
        Finall_phone = soup_phone[0].find_all(name="div")
    #print(len(Finall_phone))


    #第一个
        Finall_phone_1 = Finall_phone[0].find_all('a')
    #print(Finall_phone[0].get('a'))
        #print(Finall_phone_1[0].get("href"))
        print(Finall_phone_1[0].get_text().replace('\n', '').replace('\r', '').strip())
    #
        Finall_phone_2 = Finall_phone[1].find_all('a')
        print(Finall_phone_2[0].get_text().replace('\n', '').replace('\r', '').strip())
        print(i," ",soup.name[i].get_text().replace('\n', '').replace('\r', '').strip(),"完成")

        with open("./data_2.csv", 'a',newline='') as f:#a表示在文末追加，newline用于去除间隔的空行
            writer =   csv.writer(f)
            writer.writerows([[soup.name[i].get_text().replace('\n', '').replace('\r', '').strip(),(Finall_phone_1[0].get_text().replace('\n', '').replace('\r', '').strip()),(Finall_phone_2[0].get_text().replace('\n', '').replace('\r', '').strip())]])# 写入多行用writerows，一次在一行写入三个数值




"""
    (508) 255-6000


                    (508) 237-2771
"""


if __name__ == "__main__":
    #for i in range(1,16):
        #Get_url("https://www.gibsonsothebysrealty.com/agents?page=",i)
    with open("./data_2.csv", 'a',newline='') as f:#a表示在文末追加，newline用于去除间隔的空行
          writer = csv.writer(f)
          writer.writerow(["Name", "Office_numbe", "Mobile_number"])  # 先写入列名
    for i in range(1,16):
        print("Page",i," 正在开始")
        Get_info(i)
