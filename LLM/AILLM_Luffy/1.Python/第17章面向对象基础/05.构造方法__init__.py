# 声明类
class Dog:
    # 类属性
    legs_num = 4
    has_hair = True
    has_tail = True

    def __init__(self, name, breed, color, age):
        print("__init__方法被调用")
        print("self:::", id(self))
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age
    
    # def init_prop(self, name, breed, color, age):
    #     self.name = name
    #     self.breed = breed
    #     self.color = color
    #     self.age = age
    
    # 方法
    def bark(self):
        print("self:::", self)
        print(f"{self.name}正在狂吠")

    def bite(self, person):
        print(f"狗咬{person}")

    def fetch(self):
        print("狗捡球")
        
    def show_info(self):
        print(f"名字：{self.name}，品种：{self.breed}，颜色：{self.color}，年龄：{self.age}岁")

# 创建类的对象的过程：类的实例化：new 类()

# 版本一
# alex = Dog()

# alex.init_prop("Alex", "Labrador", "黄色", 3)
# alex.bark()
# alex.show_info()

"""
    类实例化步骤
    （1）开辟实例空间
    （2）调用__init__(实例空间地址)
    （3）将实例空间地址作为类的实例化的返回值
"""


# 版本二
alex = Dog("Alex", "Labrador", "黄色", 3)
print("alex:::", id(alex))
alex.show_info()
