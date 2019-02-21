row = 1
while row <= 9:

    col = 1
    while col <= row:

        print("%d * %d = %d"%(col, row, row * col), end="\t")
        col += 1
    print("")   # 这行代码就是换行的
    row += 1