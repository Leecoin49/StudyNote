# (2)__str__方法
# class Person(object):
#     def __init__(self, name, age):
#         print("_init_方法执行")
#         self. name = name
#         self. age = age

#     def __str__(self):
#         print("__str__执行...")
#         return f"姓名：{self.name} 年龄：{self.age}"

# yuan = Person("yuan", 23)
# # 触发__str__执行的是str()
# print(str(yuan))

# alex = Person("alex", 33)
# print(alex)

# （3）__eq__方法
# 案例一
class Person(object):
    def __init__(self, name, age):
        print("_init_方法执行")
        self. name = name
        self. age = age
    
    # 触发机制：==
    def __eq__(self, other):
        return self.age == other.age

yuan = Person("yuan", 33)
alex = Person("alex", 33)

print(alex == yuan)

# 案例二
class Dog(object):
    def __init__(self, name, age):
        self. name = name
        self. age = age

    def __eq__(self, other):
        print("Dog __eq__")
        return self.age == other.age

class Person(object):
    def __init__(self, name, age):
        self. name = name
        self. age = age

    def __eq__(self, other):
        print("Person __eq__")
        return self.name == other.name and self.age == other.age

yuan = Person("yuan", 23)
alex = Dog("alex", 22)

print(yuan == alex)
print(alex == yuan)