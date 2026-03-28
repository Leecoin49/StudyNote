from loguru import logger

class Cache(object):

    def __init__(self):
        # self.data = {}
        self.__dict__["data"] = {}
    
    def __setattr__(self, key, value):
        print("__setattr__:::", key, value)
        self.__dict__["data"][key] = value
        
    def __getattr__(self, key):
        return self.__dict__["data"].get(key)
    
    def __delattr__(self, key):
        # 各种操作
        self.__dict__["data"].pop(key)
        
    def show_data(self):
        print(self.__dict__["data"])
        
    def __str__(self):
        return str(self.__dict__["data"])

cache = Cache()
cache.name = "yuan"
cache.age = 18
# print(cache.__dict__)
# print(cache.name) 
# del cache.name
# cache.show_data()
print(cache)
