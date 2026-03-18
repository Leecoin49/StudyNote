s = str("Hello, world!")
print(s,type(s))
s.upper()

l = list((1,2,3))
l.append(4)
print(l)

d = dict({"k1": "v1"})
print(d)

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

alex = Dog("Alex", "Labrador", "黄色", 3)

# 任何一个实例对象都属于本身类型
print(alex)
print(type(alex))

# 自定义类型对象属于可变数据类型
alex.age = 10
print(alex.age)

# 实例对象也是一等公民，变量传递，作为函数参数，函数返回值

# 变量传递
x = alex
print(x.name)
print(x.age)
alex.age = 10000
print(x.age)

# 函数参数
def foo(x):
    print(x)
    print(type(x))
    x.append(4)
    
# a = 1000
# foo(a)
# b = [1, 2, 3]
# foo(b)
# print(b)

# def bar(y):
#     print(y, type(y))
#     y.age = 10000

# bar(alex)
# print(alex.age)

def test():
    peiQi = Dog("PeiQi", "Labrador", "黑色", 2)
    
    return peiQi

pq = test()
print(pq.name)
print(pq.age)