import base64, sys
str = 'http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c'

s = base64.urlsafe_b64decode(str)
print(s)

f = open('test.bmp', 'rb')
print(f.read())