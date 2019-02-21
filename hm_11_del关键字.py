name_list = ["Xey", "ajl", "安家樑"]

# 使用del关键字(delete)删除列表元素
del name_list[1]
# del关键字本质上是用来将一个变量从内存中删除
name = "xx"
del name
# 注意：用del删除的变量，后续不能再使用额
print(name)

print(name_list)