# 猜随机数

import random
start = input('请输入开始值： ')
end = input('请输入结束值： ')
start = int(start)
end = int(end)
r = random.randint(start, end)

count = 0
while True:
    guess = input('请输入猜测数字： ')
    count = count +1
    if guess == str(r):
        print('恭喜你，猜对了！')
        print('这是你猜的第', count, '次')
        break
    elif guess < str(r):
        print('数字小了！')
    elif guess > str(r):
        print('数字大了！')
    print('这是你猜的第', count, '次')
