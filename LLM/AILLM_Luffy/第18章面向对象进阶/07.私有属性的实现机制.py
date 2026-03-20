# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         # 私有化
#         self.__score = score

#     def test(self):
#         pass
    
#     # 开放的一个查询成绩的接口
#     def get_score(self):
#         return self.__score
    
#     def set_score(self, score):
#         if isinstance(score,int) and 0< score < 100:
#             self.__score = score
#         else:
#             raise ValueError("数据错误")



# yuan = Student("yuan", 88)

# # 案例1

# print(yuan.name)

# print(yuan.score)

# yuan.score =100

# print(yuan.score)

# 案例2

# print(yuan.name)

# print(yuon.__score)

# print(yuan.get_score())

# yuan.__score =1680

# yuan.set_score(99)

# print(yuan.get_score())



# 案例3

# class Student2:
#     def __init__(self, name, score):
#         self.name = name
#         # 私有化__score
#         self.score = score

# rain = Student2("rain", 88)

# rain.score = "hello world!"

# yuan = Student("yuan", 88)

# print(yuan._Student__score)
# yuan._Student__score=10000
# print(yuan.get_score())


# 案例

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self._score = score

class Student(Person):
    def get_score(self):
        return self.__score

    def set_score(self,score):
        self.__score=score

yuan=Student("yuan", 66)

# print(yuan.__dict__)
print(yuan.get_score())


"""
    单下划线、双下动线、头尾双下划线说明:

    __foo__:定义的是特殊方法，一般是系定义名字，似_init__()之类的。

    __foo:双下划线的表示的是私有类型(private)的变量,只能是允许这个类本身进行访问了。

    _foo:以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问。(约定成俗，不限语法)

"""
