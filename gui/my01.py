#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang

from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("我的第一个GUI")
root.geometry("500x300+100+200")
btn1 = Button(root)
btn1['text'] = '点我就送花'

btn1.pack()

def songhua(e):

    messagebox.showinfo('哈哈哈','送你一朵玫瑰花，亲亲我吧')
    print('送你99朵玫瑰花')

btn1.bind('<Button-1>',songhua)


root.mainloop()