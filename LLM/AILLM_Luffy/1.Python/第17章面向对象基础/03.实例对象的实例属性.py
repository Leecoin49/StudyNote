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

# 实例属性复制：实例对象.属性 = 值 向实例空间写入属性和值
alex.name = "李杰"
alex.age = 10
print(alex.name)
peiQi.name = "武大郎"
peiQi.age = 8
print(peiQi.name)

# (1)
alex.age = 30
print(alex.age)
print(peiQi.age)

# (2) 实例对象.变量 查询顺序 [实例空间，类空间，父类空间]
# alex.bark()
alex.bark = 1000
# alex.bark()
peiQi.bark()

alex.legs_num = 5

print(alex.legs_num)
print(peiQi.legs_num)