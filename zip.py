import zipfile

def extractFile(zipFile, password):
    try:
        zipFile.extractall(pwd= bytes(password, "utf8" ))
        print("李大伟的压缩包密码是" + password)  #破解成功
    except:
        pass  #失败，就跳过

def main():
    zipFile = zipfile.ZipFile('李大伟.zip')
    PwdLists = open('passdict.txt')   #读入所有密码
    for line in PwdLists.readlines():   #挨个挨个的写入密码
        Pwd = line.strip('\n')
        guess = extractFile(zipFile, Pwd)

if __name__ == '__main__':
    main()

花了不到一分钟

成功解出密码是：



​

收工√

趁着李大伟还没回来，

多说两句。

李大伟设置的只是6位数字的密码，

所以本次只要单线程暴力遍历就ok了。

那如果更多位数，

字母数字特殊字符混合的复杂密码呢？

我们可以应用多线程进程解压，加快速度

网络上还有一些暴力破解字典，

可以下载用来遍历

感兴趣的朋友们不妨试试。

大伟回来了。

我告诉他密码就是压缩包当天的日期。

李大伟表示：20191119他已经试过了。

然而这个压缩包的压缩时间是前一天20191118啊。

你口口声声说用当天日期，拿今天1119试什么试？



​

不过奶茶真好喝~

相关破解源码和李大伟压缩包已上传Github：https://github.com/zpw1995/aotodata/tree/master/interest/zip



作者 | 朱小五

又是一杯奶茶。

事情的经过是这样的：





又是奶茶，行吧行吧。

快点开工，争取李大伟回来之前搞定。

李大伟说是6位数字密码

那么我们可以利用python生成全部的六位数字密码

#生成从000000到99999的密码表
f = open('passdict.txt','w')
for id in range(1000000):
    password = str(id).zfill(6)+'\n'
    f.write(password)
f.close()
这样，我们就生成了一个从000000到99999的密码表。

并把它们存入到 passdict.txt 的文件中。



6位的密码表就这么大！！！

下一步做什么？

自然是将生成的密码表中的密码遍历，

暴力破解啦！

科普时间：

zipFile模块式Python自带的模块，提供了对zip 文件的创建，读，写，追加，解压以及列出文件列表的操作

解压使用extractll方法extractall(path=None, members=None, pwd=None)

path：指定解压后文件的位置

members:（可选）指定要Zip文件中要解压的文件，这个文件名称必须是通过namelist()方法返回列表的子集

pwd：指定Zip文件的解压密码

那么我们可以利用 zipFile 模块来遍历密码表，

挨个挨个密码尝试，看能不能打开压缩包。

直到成功。

导入zipFile

import zipfile

def extractFile(zipFile, password):
    try:
        zipFile.extractall(pwd= bytes(password, "utf8" ))
        print("李大伟的压缩包密码是" + password)  #破解成功
    except:
        pass  #失败，就跳过

def main():
    zipFile = zipfile.ZipFile('李大伟.zip')
    PwdLists = open('passdict.txt')   #读入所有密码
    for line in PwdLists.readlines():   #挨个挨个的写入密码
        Pwd = line.strip('\n')
        guess = extractFile(zipFile, Pwd)

if __name__ == '__main__':
    main()
花了不到一分钟

成功解出密码是：



收工√

趁着李大伟还没回来，

多说两句。

李大伟设置的只是6位数字的密码，

所以本次只要单线程暴力遍历就ok了。

那如果更多位数，

字母数字特殊字符混合的复杂密码呢？

我们可以应用多线程进程解压，加快速度

网络上还有一些暴力破解字典，

可以下载用来遍历

感兴趣的朋友们不妨试试。

大伟回来了。

我告诉他密码就是压缩包当天的日期。

李大伟表示：20191119他已经试过了。

然而这个压缩包的压缩时间是前一天20191118啊。

你口口声声说用当天日期，拿今天1119试什么试？



不过奶茶真好喝~

相关破解源码和李大伟压缩包已上传Github：https://github.com/zpw1995/aotodata/tree/master/interest/zip

标签: Python
好文要顶 关注我 收藏该文
Python学习啊
关注 - 0
粉丝 - 14
+加关注
10
« 上一篇： python常见错误
» 下一篇： Python定做一个计算器，小而美哒~
posted @ 2019-12-17 13:53  Python学习啊  阅读(179)  评论(0)  编辑  收藏
