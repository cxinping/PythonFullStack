# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="xinpingedu@163.com"    #用户名
mail_pass="123welcome"   #口令

sender =mail_user
receivers = [ 'xpws2006@163.com' ]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.cnblogs.com">这是一个链接,跳转到博客园</a></p>
"""

message = MIMEText(mail_msg , 'html', 'utf-8')
message['From'] = Header("测试邮件标题", 'utf-8')
message['To'] =  ";".join(receivers)

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.close()
    print( "邮件发送成功")
except Exception as e :
    print( "Error: 无法发送邮件")
    print( str(e) )
