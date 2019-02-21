# 1. 输入单价
price = input("请输入苹果单价：")
# 2. 输入重量
weight = input("请输入苹果重量：")
# 3. 计算支付金额
# 注意：两个字符串之间不能直接用乘法
'''
将单价重量转换成小数
'''
price = float(price)
weight = float(weight)
money = price * weight
print("苹果总金额：", money)