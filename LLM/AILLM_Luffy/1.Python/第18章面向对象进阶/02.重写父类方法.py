class Animal():
    def eat(self):
        print("eating...")

    def sleep(self):
        print("self:::", id(self))
        print("sleep...")

class Dog(Animal):
    def swimming(self):
        print("swimming...")
        
    def sleep(self): # 重写父类方法
        # print("dog sleep...")
        # 调用父类方法
        # 方式1：类对象.方法(self, 其他参数)
        # Animal.sleep(self)
        # 方式2：super()
        super().sleep()
        print("侧翻睡")
        
alex = Dog()
print(id(alex))
alex.sleep()