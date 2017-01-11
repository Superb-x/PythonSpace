#准确的讲， Python没有专门处理字节的数据类型。但是由于b'str'可以表示字节，所以，字节数组=二进制str，而在C语言中，我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换。
# 在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的bytes，你得配合位运算符这么写：
#
# >>> n = 10240099
# >>> b1 = (n & 0xff000000) >> 24
# >>> b2 = (n & 0xff0000) >> 16
# >>> b3 = (n & 0xff00) >> 8
# >>> b4 = n & 0xff
# >>> bs = bytes([b1, b2, b3, b4])
# >>> bs
# b'\x00\x9c@c'
# 非常麻烦。如果换成浮点数就无能为力了。

#Python的struct模块用来解决bytes和其他二进制数据类型的转换
#struct的pack()函数可以把任意数据变成bytes
import struct, sys
print(struct.pack('>I', 10240099))
f = open('test.bmp', 'rb')
print(struct.unpack('ccIIIIIIHH', f.read()))


