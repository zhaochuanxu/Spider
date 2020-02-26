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


def Catch_url(N):
   name = "./elliman/elliman_"+str(N)+".txt"
   with open(name,'r',encoding='utf-8') as f:
      s = f.read()
   #print(s)


   soup = BeautifulSoup(s,'html.parser')


        #然后使用soup的属性
  # soup.all = soup.find_all(name="tbody")
   #soup.name = soup.find_all(name='td',attrs={"class":"first"})

   soup.Email = soup.find_all(name='td',attrs={"class":"last"})#获取邮箱
   soup.name = soup.find_all(name='td',attrs={"class":"first"})
   soup.phone = soup.find_all(name = 'tbody')
   p = soup.phone[0].find_all("tr")
      #p =soup.phone[0].find_all("tr")
   #找到所有的tr

   #print(len(p)) #3个
   #for i in range(0,len(len(p))):

   #print(len(phone))
   with open("./data_1.csv", 'a',newline='') as f:#a表示在文末追加，newline用于去除间隔的空行
      writer = csv.writer(f)
          #writer.writerow(["姓名", "邮箱", "电话"])  # 先写入列名
      sshkl = N+"开头"
      writer.writerow([str(sshkl), "" , ""])


   #print(soup.name[1].get_text('a'))  #获取姓名
   num = len(soup.Email)
   for i in range(0,num):
       name_Len =0
       mail_Len =0
       name_1 = str(soup.name[i].get_text('a')).replace('\n', '').replace('\r', '')
       mail_1 = str(soup.Email[i].get_text('a')).replace('\n', '').replace('\r', '')
       name_Len =int(len(name_1))
       mail_Len =int(len(mail_1))
       #print(mail_Len)
       #print(name_1[1:len(name_1)-1])

       Finall_name=name_1[1:len(name_1)-1]
       # print(name_1[1,name_Len-1])
       #print(mail_1[1:len(mail_1)-1])
       Finall_mail = mail_1[1:len(mail_1)-1]


       p_1 = p[i].find_all('td')
       Finall_phone = str(p_1[2].get_text()).replace('\n', '').replace('\r', '')
       #print(Finall_phone)



       with open("./data_1.csv", 'a',newline='') as f:#a表示在文末追加，newline用于去除间隔的空行
          writer = csv.writer(f)
          #writer.writerow(["姓名", "邮箱", "电话"])  # 先写入列名

          writer.writerows([[Finall_name,Finall_mail,Finall_phone]])# 写入多行用writerows，一次在一行写入三个数值







if __name__ == "__main__":
    #Get_url("https://www.elliman.com/agents/massachusetts/")
   #for i in range(ord("a"),ord("z")):
       #print(chr(i))  //循环遍历i
      #url = "https://www.elliman.com/agents/massachusetts/"+chr(i)
      #print(url)
      #Get_url(url)
    #Get_info()]
    with open("./data_1.csv", 'a',newline='') as f:#a表示在文末追加，newline用于去除间隔的空行
        writer = csv.writer(f)

        writer.writerow(["姓名", "邮箱", "电话"])  # 先写入列名
    for i in range(ord('a'),ord('e')):
        Catch_url(chr(i))
    for i in range(ord('f'),ord('i')):
        Catch_url(chr(i))
    for i in range(ord('j'),ord('q')):
        Catch_url(chr(i))
    for i in range(ord('r'),ord('u')):
        Catch_url(chr(i))#t有
        Catch_url(chr(i))#t有

    for i in range(ord('y'),ord('z')):#v没有
        Catch_url(chr(i))
    Catch_url('z')