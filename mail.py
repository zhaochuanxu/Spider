#! /usr/bin/python3
# coding=utf-8 
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'iamzhouling@163.com' # input('From: ')
password = 'XXXXXX # input('Password: ')这里填入发件人邮箱客户端授权码
to_addr = '1750752919@qq.com' # input('To: ')
smtp_server = 'smtp.163.com'# input('SMTP server: ')

msg = MIMEText('hello, this message is sent by Python in Aug...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python lover <%s>' % from_addr)# 发件人
msg['To'] = _format_addr('163 manager <%s>' % to_addr)# 收件人
msg['Subject'] = Header('from SMTP……', 'utf-8').encode()
    
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
