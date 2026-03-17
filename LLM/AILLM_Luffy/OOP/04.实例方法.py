# 声明类
class Dog:
    # 类属性
    legs_num = 4
    has_hair = True
    has_tail = True

    # 方法
    def bark(self):
        print("self:::", self)
        print(f"{self.name}正在狂吠")

    def bite(self, person):
        print(f"狗咬{person}")

    def fetch(self):
        print("狗捡球")

# 创建类的对象的过程：类的实例化：new 类()

alex = Dog()
peiQi = Dog()

# (1)self
# print("alex:::", alex)
# alex.bark()
# peiQi.bark()

# alex.bite("yuan")
# alex.bite("rain")

# (2)
alex.name = "李杰"
alex.age = 10
alex.bark()
# peiQi.bark()