#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang

from tkinter import *
from  tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        '''
        创建组件
        :return:
        '''

        self.lable01 = Label(self,text="百战程序员", width= 10, height=2, bg='black', fg='white')
        self.lable02 = Label(self,text="胡成强", width= 10, height=2, bg='blue', fg='white',
                             font=('黑体',30))
        self.lable01.pack()
        self.lable02.pack()

if __name__ == '__main__':
    root = Tk()
    root.geometry('400x400+100+200')
    app = Application(master=root)
    root.mainloop()
