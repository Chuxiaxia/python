# 打印小星星
# 1. 定义一个计数器变量， 从数字1开始， 循环方便
row = 1
# 2. 开始循环
while row <= 5:

    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    print("")   # 这行代码就是换行的
    row += 1