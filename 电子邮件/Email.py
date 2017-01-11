from email.mime.text import MIMEText
msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8')
print(msg)
#创建之后下一步就是发送出去了
#输入Email地址和口令：
from_addr = input('From: ')
pwd = input('Password: ')
#输入收件人地址
to_addr = input('To: ')
#输入SMTP服务器地址
smtp_server = input('SMTP server: ')

import smtplib
server = smtplib.SMTP(smtp_server, 25) #默认端口是25
server.set_debuglevel(1)
server.login(from_addr, pwd)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()