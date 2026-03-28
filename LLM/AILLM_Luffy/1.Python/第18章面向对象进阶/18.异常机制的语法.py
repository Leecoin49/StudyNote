# (1) 通用异常
try:
    pass #正常执行语句
except Exception as ex:
    pass #异常处理语句

# (2) 指定异常
try:
    pass #正常执行语句
except <异常名>:
    pass #异常处理语句

# (3) 统一处理多个异常
try:
    pass #正常执行语句
except(<异常名1>, <异常名2>, ...):
    pass #异常处理语句

# (4) 分别处理不同的异常
try:
    pass #正常执行语句
except <异常名1>:
    pass #异常处理语句1
except <异常名2>:
    pass #异常处理语句2
except<异常名3>:
    pass #异常处理语句3

# (5) 完整语法
try:
    pass #正常执行语句
except Exception as e:
    pass #异常处理语句
else:
    pass # 测试代码没有发生异常
finally:
    #无论是否发生异常一定要执行的语句,比如关闭文件，数据库或者socket
    pass