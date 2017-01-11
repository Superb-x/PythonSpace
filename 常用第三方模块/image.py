from PIL import Image, ImageFilter

#打开一个JPG图像文件
im = Image.open('BENZ.jpg')
#获得图像尺寸
w, h = im.size
print('Original size is %s * %s' % (w, h))
im.thumbnail((w//2, h//2))
print('Resize size is %s * %s' % (w//2, h//2))
#把缩放后的图片用jpeg格式保存
im.save('thumbnail.jpg', 'jpeg')

#添加模糊效果
img = Image.open('thumbnail.jpg')
img2 = im.filter(ImageFilter.BLUR)
img2.save('blur.jpeg', 'jpeg')