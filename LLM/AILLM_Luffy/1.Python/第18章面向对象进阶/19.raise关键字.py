# 案例1
# def a():
#     print("aaa")
#     b()
    
# def b():
#     print("aaa")
#     c()
    
# def c():
#     yuan
#     print("aaa")
    
# print(123)
# print(123)
# print(123)
# a()
# print(123)
# print(123)
# print(123)

# 案例2
class CouponError01(Exception):
    def __init__(self):
        print("优惠券错误类型1")
        
class CouponError02(Exception):
    def __init__(self):
        print("优惠券错误类型2")
        
class CouponError03(Exception):
    def __init__(self):
        print("优惠券错误类型3")
        
def main():
    try:
        choice = input(">>>")
        
        if choice == "1":
            # 出现优惠券错误类型1
            raise CouponError01()
        elif choice == "2":
            # 出现优惠券错误类型2
            raise CouponError02()
        elif choice == "3":
            # 出现优惠券错误类型3
            raise CouponError03()
        
    except CouponError01 as e:
        print("解决优惠券错误类型1")
        
    except CouponError02 as e:
        print("解决优惠券错误类型2")
        
    except CouponError03 as e:
        print("解决优惠券错误类型3")

if __name__ == '__main__':
    main()