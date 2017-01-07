#编写一个程序，能实现当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出绝对路径\
import os

def search(str_name, path_x):
    for x in os.listdir(path_x):
        path_y = os.path.join(path_x, x)
        if os.path.isfile(path_y) and str_name in os.path.split(path_y)[1]:
            print(path_y)
        elif os.path.isdir(path_y):
            search(str_name, path_y)

if __name__ == '__main__':
    search('test.txt', '.')