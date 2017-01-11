#摘要算法简介
#Python的haslib提供了常见的摘要算法，比如MD5，SHA1等等
import hashlib

md5 = hashlib.md5()
md5.update('How to use md5 in Python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
#只要改动一个字符，计算结果就完全不同

#另一种摘要算法是SHA1，调用SHA1和调用MD5完全类似

sha1 = hashlib.sha1()
sha1.update('How to use sha1 in '.encode('utf-8'))
sha1.update('Python hashlib'.encode('utf-8'))
print(sha1.hexdigest())

#比SHA1更安全的算法是SHA256、SHA512，不过越安全的算法不仅速度越慢，而且摘要长度更长