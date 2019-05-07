#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang

'''
    设计模式
'''

class Benz():
    print("创建奔驰")

class BMW():
    print("创建宝马")

class BYD():
    print("创建比亚迪")

class CarFactory():
    '''
        测试工厂模式
    '''
    def creat_car(self, brand):
        if brand == "奔驰":
            return Benz()
        elif brand == "宝马":
            return BMW()
        elif brand == "比亚迪":
            return BYD()
        else:
            return "未知品牌，无法创建"

class Mysingleton:
    '''
        单例设计模式
        单例模式(Singleton Pattern)的核心作用是确保一个类只有一个实例，并且提供一 个访问该实例的全局访问点
    '''
    __obj = None
    __init_flag = True
    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)
        return cls.__obj
    def __init__(self,name):
        if Mysingleton.__init_flag :
            print("init")
            self.name = name
            Mysingleton.__init_flag = False



class Singleton_Factory:
    '''
    单例工厂模式
    '''
    __obj = None
    __init_flag = True

    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)
        return cls.__obj

    def __init__(self):
        if Singleton_Factory.__init_flag:
            print("单例工厂")
            Singleton_Factory.__init_flag = False

    def creat_car(self, brand):
        if brand == "奔驰":
            return Benz()
        elif brand == "宝马":
            return BMW()
        elif brand == "比亚迪":
            return BYD()
        else:
            return "未知品牌，无法创建"
        

