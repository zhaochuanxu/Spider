import os
import bs4
import requests
import re
from bs4 import BeautifulSoup
import  time
import hashlib



#Python Imaging Library，已经是Python平台事实上的图像处理标准库
# Pillow是PIL的一个派生分支，但如今已经发展成为比PIL本身更具活力的图像处理库。
import PIL


#设置自动更新桌面背景必须


#获取网页内容
def catch(url,times):

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

        #查看网页编码方式
        # #print(rps.content) 注意这编码方式为返回的是bytes型的原始数据
       # print(rps.text)

        #soup = BeautifulSoup(rps.text, 'lxml')
       # print(soup.img.string)

    if times==0: #第一次爬取网站
        Get_pic(rps) #爬取所有图片
        global old_Web_content
        old_Web_content = rps.text  #初始化网页内容
        soup = BeautifulSoup(rps.text,'html.parser')
        soup.font = soup.find_all('h3')
        global describe_Zero
        describe_Zero= str(soup.font[0].get_text())



    else:
        new_Web_content = rps.text
        #temp = Judge_update(old_Web_content,new_Web_content,rps)
        soup = BeautifulSoup(rps.text,'html.parser')
        soup.font = soup.find_all('h3')
        describe_One = soup.font[0].get_text()
        if str(describe_One) ==str(describe_Zero):
            print("网站首页还未更新，无法抓取最新信息,软件正在休眠")

            #print("下载另一页面")
            #catch('https://bing.ioliu.cn/?p=2',0)
           # time.sleep(30000)





#获取内容中的标签 并下载图片
def Get_pic(rps):

       # 首先使用Beautifulsoup()把获取的网页源码交给Beautifulsoup处理。
        soup = BeautifulSoup(rps.text,'html.parser')


        #然后使用soup的属性
        soup.img = soup.find_all('img')
       # print(soup.img)
        #抓取所有h3
        soup.font = soup.find_all('h3')
       ## print(type(soup.font[1]))
       # print(str(soup.font[1]))
       #获取文本内容
       # print(soup.font[1].get_text())  #




 #class 'bs4.element.ResultSet'>  这里是字典外套了一个列表  textPid = pid[0]
        #print(type(soup.img)) <class 'bs4.element.ResultSet'>

        #获取这个第一个标签
        #print(soup.img[0])
        #获取这个标签一共个数
        #print(len(soup.img))
        #获取这个标签 里边src内容
        #print(soup.img[1]['scr'])

        #获取这个属性下的东西
        #print(soup.img['src'])

        #rsp = requests.get(soup.img['src'])
        #with open("new.jpg",'wb')as jpg:
            #jpg.write(rsp.content)  #注意以字节写入

        for i in range (0,len(soup.img)):
           describe = soup.font[i].get_text()
           name = soup.img[i]['src']

           name = re.findall(r'\d+',name)  #findall是找多个列表格式 search是group  所以第一个是r[0]

           #print(describe) #图片描述
           #print(name[1])唯一标识
           path = './Picture'
           #os.mkdir(path)
           isExists = os.path.exists(path)
           if not isExists:
              os.makedirs(path)
           path = path +'/'+ str(name[1])#创建文件夹
           isExists = os.path.exists(path)
           if not isExists:
              os.makedirs(path)
           describe_path = path+"/describe.txt"##进入文件夹
           path = path+'/'+str(name[1])#进入自己文件夹创建名字

           path = path +'.jpg'
           with open(path,"wb") as jpg:
              rsp = requests.get(soup.img[i]['src']) #获取
              jpg.write(rsp.content)
           #print(describe_path)
           #print(str(describe))
           with open(describe_path,'w',encoding='utf-8') as txt:
               txt.write(str(describe))





          # with open(name,"wb") as jpg:
              #rsp = requests.get(soup.img[i]['src']) #获取
              #jpg.write(rsp.content)




#判断两个网页内容是否一致
def Judge_update(old_content,new_content,rps):

    #md5 = hashlib.md5()
    #old_md5 = md5.update(old_content.encode('utf-8'))
    #print(old_md5.hexdigest())
    soup = BeautifulSoup(rps.text,'html.parser')
    soup.font = soup.find_all('h3')






#def judge_finish():
    




if __name__=="__main__":
    times = 0
    while True:

        url = "https://bing.ioliu.cn/"
        catch(url,times)
        times =times + 1
        print(times)

