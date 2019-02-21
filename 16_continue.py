i = 0
while i < 10:
    # continue 某一条件满足时，不再执行后续重复代码
    if i == 3:
        #在使用这个关键字之前，需要确认循环的计数是否修改
        #否则可能会导致死循环
        i += 1
        continue
    print(i)
    i += 1
print("over~")