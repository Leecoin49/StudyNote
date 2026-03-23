class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

yuan = Person("yuan", 18, "male")

# 对象.属性变量
print(yuan.name)
yuan.age = 100
print(yuan.age)

while 1:
    attr = input("请输入您想查询的yuan的某个属性:\n")

    # print(yuan.attr)
    # # 方案1
    # if attr == "name":
    #     print(yuan.name)
    # elif attr == "age":
    #     print(yuan.age)
    # elif attr == "gender":
    #     print(yuan.gender)
    # else:
    #     print("输入有误")
        
    """
        在Python中，反射是指在运行时通过名称字符串来访问、检查和操作对象的属性和方法的能力。
        Python提供了一些内置函数和特殊方法，使得可以动态地获取对象的信息并执行相关操作。
    """
    # print(getattr(yuan, "name"))
    # print(getattr(yuan, "age"))
    
    if hasattr(yuan, attr):
        val = getattr(yuan, attr)
        print(f"yuan的{attr}的属性值：{val}")
    else:
        print(f"yuan没有{attr}属性")
        choice = input("是否给yuan加入该属性【Y/N】")

        if choice.lower()=="y":
            value = input(f"请输入yuan对象{attr}一个确定值:")

            setattr(yuan, attr, value)

