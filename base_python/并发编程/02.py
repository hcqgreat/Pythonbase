#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang

from multiprocessing import Process

def run_test():

    print("-----test----")

if __name__ == '__main__':
    print('主进程')
    p = Process(target=run_test)
    p.start()
