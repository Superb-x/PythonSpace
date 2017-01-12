from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

import poplib

#只需要一行代码把邮件内容解析成Message对象
email = '172564615@qq.com'
password = 'isykoqzfmwoibieh'
pop3_server = 'pop.qq.com'

#连接到服务器
server = poplib.POP3_SSL(pop3_server)
#打开调试信息
server.set_debuglevel(1)
#打印pop欢迎文字
print(server.getwelcome().decode('utf-8'))

#身份认证
server.user(email)
server.pass_(password)

#stat返回邮件数量及占用空间
print('Message %s size: %s' % server.stat())
#list()返回所有邮件编号
resp, mails, octects = server.list()
#可以查看返回的列表
print(mails)

#获取最新的一封邮件,索引从1开始
index = len(mails)
print(server.retr(index))
resp, lines, octects = server.retr(index)
#获得整个邮件的原始文件
msg_content = b'\r\n'.join(lines).decode('utf-8')
msg = Parser().parsestr(msg_content)
#关闭连接
server.quit()

#这个Message对象本身可能是一个MIMEMultipart对象，即包含嵌套的其他MIMEBase对象，嵌套可能还不止一层。

#所以我们要递归地打印出Message对象的层次结构
#indent 用于缩进显示
# indent用于缩进显示:
def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

#文本邮件的内容也是str，还需要检测编码，否则，非UTF-8编码的邮件都无法正常显示：
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset
