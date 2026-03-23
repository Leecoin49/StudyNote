from loguru import logger

# (1)属性装饰器
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

# # 版本1
# print(yuan.get_score())
# yuan.set_score(99)
# print(yuan.get_score())

# 版本2
# class Student:
#     def __init__(self, name, score):
#         self.__name = name
#         # 私有化
#         self.__score = score

#     def test(self):
#         pass
    
#     # 开放的一个查询成绩的接口
#     @property
#     def score(self):
        
#         logger.info(f"{self.__name}查询了成绩:{self.__score}")
        
#         return self.__score
    
#     @score.setter
#     def score(self, score):
#         if isinstance(score,int) and 0< score < 100:
#             self.__score = score
#         else:
#             raise ValueError("数据错误")
        
# yuan = Student("yuan", 88)
# print(yuan.score)
# yuan.score = 99
# print(yuan.score)

# 版本3
# (1)属性装饰器
class Student:
    def __init__(self, name, score):
        self.name = name
        # 私有化
        self.__score = score

    def test(self):
        pass
    
    # 开放的一个查询成绩的接口
    def __get_score(self):
        return self.__score
    
    def __set_score(self, score):
        if isinstance(score,int) and 0< score < 100:
            self.__score = score
        else:
            raise ValueError("数据错误")

    score = property(__get_score, __set_score)


yuan = Student("yuan", 88)
print(yuan.score)
yuan.score = 99
print(yuan.score)