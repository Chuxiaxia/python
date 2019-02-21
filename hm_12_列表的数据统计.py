name_list = ["Xey", "ajl", "安家樑", "Xey"]

# len(length长度)函数可以统计列表中元素的总数
list_len = len(name_list)
print("列表中包含%d个元素" % list_len)
# count方法可以统计列表中某一个数据出现的次数
count = name_list.count("Xey")
print("Xey出现了%d次" % count)
# 从列表中删除第一次出现的数据，如果数据不存在程序会报错
name_list.remove("Xey")
print(name_list)