class AliPay:
    def pay(self):
        print('通过支付宝消费')

class WeChatPay:
    def pay(self):
        print("通过微信消费")

class Order(object):
    def account(self,pay_obj):
        pay_obj.pay()
        
class YinLianPay:
    def pays(self):
        print("通过银联消费")

# pay1=WeChatPay("yuan", 188)
# pay2=AliPay("alvin", 288)

pay1=WeChatPay()
pay2=AliPay()
pay3=YinLianPay()

order = Order()
order.account(pay1)
order.account(pay2)
order.account(pay3)
