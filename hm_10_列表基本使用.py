name_list = ["xey", "ajl", "xx"]

# 1. 取值和取索引
print (name_list[2])
# 知道数据的内容，想确定数据在列表的位置
# 使用index方法需要注意，如果传递的数据不在列表中，程序会报错。
print(name_list.index("xey"))

# 2. 修改
# 注意： 列表指定的索引超出范围，程序会报错
name_list[1] = "安家樑"

# 3. 增加
# append方法可以向列表末尾增加数据
name_list.append("夏夏")
# insert方法可以在列表的指定索引位置插入数据
name_list.insert(1, "an")
# extend方法可以把另外一个列表中的完整内容追加在当前列表的末尾
temp_list = ["xu", "jiujiu"]
name_list.extend(temp_list)

# 4. 删除
# remove方法可以移除列表中任意一个数据
name_list.remove("xu")
# clear可以清空列表
name_list.clear()
# pop默认删除列表最后一个元素
name_list.pop()
# pop可以指定删除元素的索引
name_list.pop(1)

print (name_list)