i = 0
while i < 10:
    # break 某一条件满足时，退出循环，不再执行后续代码
    if i == 3:
        break
    print(i)
    i += 1
print("over~")