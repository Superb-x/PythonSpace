'''
POP3收取邮件

阅读: 2699
SMTP用于发送邮件，如果要收取邮件呢？

收取邮件就是编写一个MUA作为客户端，从MDA把邮件获取到用户的电脑或者手机上。收取邮件最常用的协议是POP协议，目前版本号是3，俗称POP3。

Python内置一个poplib模块，实现了POP3协议，可以直接用来收邮件。

注意到POP3协议收取的不是一个已经可以阅读的邮件本身，而是邮件的原始文本，这和SMTP协议很像，SMTP发送的也是经过编码后的一大段文本。

要把POP3收取的文本变成可以阅读的邮件，还需要用email模块提供的各种类来解析原始文本，变成可阅读的邮件对象。

所以，收取邮件分两步：

第一步：用poplib把邮件的原始文本下载到本地；

第二部：用email解析原始文本，还原为邮件对象。

'''
from email.parser import Parser
import poplib, sys, base64

#输入邮件地址， 口令和pop3服务器地址
email = '172564615@qq.com'
password = 'isykoqzfmwoibieh'
pop3_server = 'pop.qq.com'

#连接到POP3服务器
server = poplib.POP3_SSL(pop3_server)
#可以打开或关闭调试信息
server.set_debuglevel(1)
#可选  打印pop3的欢迎文字
print(server.getwelcome().decode('utf-8'))

#身份认证
server.user(email)
server.pass_(password)

#stat()返回邮件数量和占用空间
print('Message %s. size: %s' % server.stat())
#list()返回所有邮件的编号
resp, mails, octets = server.list()
# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
print(mails)

#获取最新一封邮件，注意索引号从1开始
index = len(mails)
resp, lines, octets = server.retr(index)
# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 稍后解析出邮件:
msg = Parser().parsestr(msg_content)
print(type(msg))
f = open('email.html', 'w')
f.write(msg_content)
# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:
server.quit()