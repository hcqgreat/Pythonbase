#! env/bin/python
#  coding : utf-8
#  auther : Hu Chengqiang

'''
    设计模式
    23种设计模式，可分为3大类型，即：
    创建型

        1. Factory Method（工厂方法）

        2. Abstract Factory（抽象工厂）

        3. Builder（建造者）

        4. Prototype（原型）

        5. Singleton（单例）

    结构型

        6. Adapter Class/Object（适配器）

        7. Bridge（桥接）

        8. Composite（组合）

        9. Decorator（装饰）

        10. Facade（外观）

        11. Flyweight（享元）

        12. Proxy（代理）

    行为型

        13. Interpreter（解释器）

        14. Template Method（模板方法）

        15. Chain of Responsibility（责任链）

        16. Command（命令）

        17. Iterator（迭代器）

        18. Mediator（中介者）

        19. Memento（备忘录）

        20. Observer（观察者）

        21. State（状态）

        22. Strategy（策略）

        23. Visitor（访问者）
'''

class Benz():
    print("创建奔驰")

class BMW():
    print("创建宝马")

class BYD():
    print("创建比亚迪")

class CarFactory(object):
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

class MysingletonOne(object):
    '''
        单例设计模式  ----> 第一种
        单例模式(Singleton Pattern)的核心作用是确保一个类只有一个实例，并且提供一 个访问该实例的全局访问点
    '''
    __obj = None
    __init_flag = True
    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)
        return cls.__obj
    def __init__(self,name):
        if MysingletonOne.__init_flag :
            print("init")
            self.name = name
            MysingletonOne.__init_flag = False

class MysingletonTwo(object):
    '''
        单例设计模式 ----> 第二种
    '''

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            org = super(MysingletonTwo, cls)
            cls._instance = org.__new__(cls)

        return cls._instance

if __name__ == '__main__':
    class SingleSpam(MysingletonTwo):
        def __init__(self, s):
            self.s = s
        def __str__(self):
            return self.s


    s1 = SingleSpam('spam')
    print(id(s1), s1)
    s2 = SingleSpam('spa')
    print(id(s2), s2)
    print(id(s1), s1)





class Singleton_Factory(object):
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
        

