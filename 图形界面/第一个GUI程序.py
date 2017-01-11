#导入tkinter包内所有的内容
from tkinter import *
import tkinter.messagebox as messagebox

#从Frame派生出一个Application类，这是所有Widget的父容器
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello ', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get()
        messagebox.showinfo('Message', 'Hello, %s' % name)
app = Application()
#设置窗口标题
app.master.title('Hello, world')
#主消息循环
app.mainloop()