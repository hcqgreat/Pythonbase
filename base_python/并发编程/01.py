#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang

from time import sleep

def sing():
    for i in range(5):
        print("正在唱歌%d" % i)
        sleep(1)

def dance():
    for i in range(5):
        print('正在跳舞%d' % i)
        sleep(1)

if __name__ == '__main__':
    sing()
    dance()


