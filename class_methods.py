class MyClass(object):
    # 实例方法
    def instance_method(self):
        print('instance method called', self)
    
    # 类方法
    @classmethod
    def class_method(cls):
        print('class method called', cls)
    
    # 静态方法
    @staticmethod
    def static_method():
        print('static method called')

class Sclass(MyClass):
#    def instance_method(self):
#        print ('son instance method called', self)
#    @classmethod
#    def class_method (cls):
#        print ('son class method called', cls)

#    @staticmethod
#    def static_method():
#        print ('son static method called')
    def son(self):
        print('why there is a need to add something new', self)
        

my_class = MyClass()        # 实例化
my_class.instance_method()  # 实例方法
my_class.class_method()     # 类方法
my_class.static_method()    # 静态方法

son_class = Sclass()
son_class.instance_method()
son_class.class_method()
son_class.static_method()

son_class.son()
