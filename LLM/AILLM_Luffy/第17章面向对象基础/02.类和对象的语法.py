# 声明类
class Dog:
    # 类属性
    legs_num = 4
    has_hair = True
    has_tail = True

    # 方法
    def bark(self):
        print("够狂吠")

    def bite(self):
        print("狗咬人")

    def fetch(self):
        print("狗捡球")

# 创建类的对象的过程：类的实例化：new 类()

alex = Dog()
peiQi = Dog()

# (1) alex和peiQi的内存地址一样吗？
print(id(alex))
print(id(peiQi))
print(alex == peiQi)

# (2) 实例对象通过句点符号调用类的属性和方法
print(alex.legs_num)
print(alex.has_tail)
alex.bark

# (3) 调用类属性一定是同一个空间值
print(id(alex.legs_num))
print(id(peiQi.legs_num))
print(id(alex.bite))
print(id(peiQi.bite))