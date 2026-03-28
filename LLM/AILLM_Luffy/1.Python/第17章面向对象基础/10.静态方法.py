class Cal(object):
    @staticmethod
    def add(x,y):
        return x+y
    
    @staticmethod
    def mul(x,y):
        return x*y

# 调用
c = Cal()
print(c.add(10, 20))

# 类对象调用
print(Cal.add(23, 45))