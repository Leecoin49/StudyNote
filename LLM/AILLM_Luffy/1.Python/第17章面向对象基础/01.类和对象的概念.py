class Person:
    name = ""
    gender = ""
    age = 0
    
    def say(self):
        print("Hello, my name is",self.name)
        
    def sleep(self):
        print("I am sleeping")
        
    def eat(self):
        print("I am eating")
        
# 初始化实例对象
zhangye = Person()
zhangye.name = "zhangye"
zhangye.gender = "male"
zhangye.age = 28

# 调用方法
zhangye.say()
zhangye.sleep()
zhangye.eat()