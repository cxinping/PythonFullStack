# -*- coding: utf-8 -*-

# Step1：以二进制格式打开一个文件用于读写
file = open('photo.jpg', 'rb' )
content = file.read()
file.close()

# Step2：以二进制格式打开一个文件只用于写入
file2 = open("photo2.jpg", "wb")
file2.write(content)
file2.close()

