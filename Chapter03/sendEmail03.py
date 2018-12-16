# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="xinpingedu@163.com"    #用户名
mail_pass="123welcome"   #口令

sender = mail_user
receivers = [ 'xpws2006@163.com' ]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


#创建一个带附件的实例
message = MIMEMultipart()

message['From'] = Header("邮件标题", 'utf-8')
message['To'] =  ";".join(receivers)
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

#邮件正文内容
message.attach(MIMEText('这是Python 邮件发送测试……', 'plain', 'utf-8'))

# 构造附件1，传送d盘下的test1.txt 文件
att1 = MIMEText(open('d:/test1.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test1.txt"'
message.attach(att1)

# 构造附件2，传送d盘下的test2.txt 文件
att2 = MIMEText(open('d:/test2.txt', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="test2.txt"'
message.attach(att2)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print( "邮件发送成功")
except Exception as e:
    print("Error: 无法发送邮件")
    print(str(e))
