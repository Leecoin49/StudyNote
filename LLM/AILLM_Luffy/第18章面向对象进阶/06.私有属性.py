class Student:
    def __init__(self, name, score):
        self.name = name
        # 私有化
        self.__score = score

    def test(self):
        pass
    
    # 开放的一个查询成绩的接口
    def get_score(self):
        return self.__score
    
    def set_score(self, score):
        if isinstance(score,int) and 0< score < 100:
            self.__score = score
        else:
            raise ValueError("数据错误")



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

yuan = Student("yuan", 88)
yuan.set_score(10000)