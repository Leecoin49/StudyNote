class Car(object):
    # 类属性
    total_cars = 0
    
    def __init__(self, make, model):
        self.make = make
        self.model = model
        print("self.__class__:", id(self.__class__))
        self.__class__.total_cars += 1
        
    # 实例方法
    def accelerate(self):
        print(f"一辆{self.make}的{self.model}正在加速")
        
    # 类方法
    @classmethod
    def show_total_cars(cls):
        print(id(cls))
        print(f"目前总共有{cls.total_cars}辆车")


print(id(Car))
Car.show_total_cars()

car1 = Car("宝马", "X5")
