# class AirConditioner:
#     def __init__(self):
#         # 初始化空调
#         pass

#     def cool(self,temperature):
#         #对外制冷功能接口方法
#         self.__turn_on_compressor()
#         self.__set_temperature(temperature)
#         self.__blow_cold_air()
#         self.__turn_off_compressor()

#     def __turn_on_compressor(self):
#         #打开压缩机(私有方法)
#         print("打开压缩机")

#     def __set_temperature(self, temperature):
#         #设置温度(私有方法)
#         print("设置温度")

#     def __blow_cold_air(self):
#         #吹冷气(私有方法)
#         print("吹冷气")

#     def __turn_off_compressor(self):
#         # 关闭压缩机(私有方法)
#         print("关闭压缩机")

# ac = AirConditioner()
# ac.cool("30度")
# ac.__turn_on_compressor()

# 案例
class Base:
    def foo(self):
        print("foo from Base")

    def test(self):
        self.foo()

class Son(Base):
    def foo(self):
        print("foo from Son")

s=Son()
s.test()

class Base:
    def __foo(self):
        print("foo from Base")

    def test(self):
        self.__foo()

class Son(Base):
    def __foo(self):
        print("foo from Son")

s=Son()
s.test()
