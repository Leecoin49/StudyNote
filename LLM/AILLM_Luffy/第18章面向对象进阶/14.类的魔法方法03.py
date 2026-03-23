# 缓存的容器类型
class Cache(object):

    def __init__(self):
        self.data = []

    def add(self, item):
        # if 环境监测 或数据判断
        self.data.append(item)

    def remove(self, item):
        self.data.remove(item)

    def show(self):
        print(self.data)

    def __len__(self):
        return len(self.data)

cache = Cache()
cache.add("yuan")
cache.add("rain")
cache.add("alvin")

cache.show()
cache.remove("yuan")
cache.show()
print(len(cache))