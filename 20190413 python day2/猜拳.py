import random
computer = random.randint(1,3)
person = int(input('人输入动作：'))
print('人输入的值',person)
print('电脑输入的值',computer)
if (computer==1 and person==2) or (computer==2 and person==3)or (computer==3 and person==1) :
    print('电脑胜')
elif computer == person :
    print('平局')
else:
    print('人获胜')