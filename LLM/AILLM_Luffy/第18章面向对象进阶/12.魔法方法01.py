# __new()__方法
# """
#     1. 开辟独立空间
#     2. 调用__init__方法
#     3. 返回该空间地址
# """

# class Person(object):
#     def __new__(cls, *args, **kwargs):
#         print("__new__方法执行")
#         return object.__new__(cls)
    
#     def __init__(self, name, age):
#         print("__init__方法执行")
#         self.name = name
#         self.age = age

# yuan =Person("yuan", 23)
# print(yuan)
# print(yuan.name)
# print(yuan.age)

# __new__方法应用

# 版本一
# class Config(object):
    
#     def __init__(self):
#         print("__init__方法执行")
        
# c1 = Config()
# c2 = Config()

# print(id(c1))
# print(id(c2))

# 版本二
class Config(object):
    instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = object.__new__(cls)
            
        return cls.instance
    
    def __init__(self):
        print("__init__方法执行")
        
c1 = Config()
c2 = Config()

print(id(c1))
print(id(c2))