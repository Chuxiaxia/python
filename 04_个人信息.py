# 在python中，定义变量时不需要指定变量类型
# 会根据语句自动推断
# str:字符串

name = input("请输入你爱的人：")
if name == "xey":
    a = "-" * 20
    print(a)
    print("姓名：", name)
    # int:整型
    age = 13
    print("年龄：", age)
    # bool:布尔类型
    gender = True  # 是
    sex = "女生"
    print("性别：%s(%s)" %(sex,gender))
    # float:小数类型，浮点数
    height = 1.58
    weight = 50.0
    print("身高：%s\n体重：%s"%(height,weight))
else:
    print("输入有误！")






