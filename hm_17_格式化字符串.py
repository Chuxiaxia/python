info_tuple = ("小明", 18, 1.75)
# 格式化字符串后面的‘（）’本质上就是元组
print("%s 年龄:%d  身高:%.2f" % info_tuple)

info_str = "%s 年龄:%d  身高:%.2f" % info_tuple
print(info_str)