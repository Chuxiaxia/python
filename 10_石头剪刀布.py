# 导入随机工具包，放在顶部
import random
print("欢迎来到石头剪刀布游戏！")
print("----------------------------")
# 电脑随机数生成random
computer = random.randint(1,3)
player = int( input("请输入你要出的拳头(1.石头 2.剪刀 3.布)："))
print("玩家：%d -- 电脑：%d"%(player,computer))
if player == computer:
    print("平局了！")
else:
    if (player==1 and computer==2) or (player==2 and computer==3) or (player==3 and computer==1):
        print("玩家胜利了！！")
    else:
        print("电脑胜利了！！")