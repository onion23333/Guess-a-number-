#猜数字小游戏

import random

print('猜数字小游戏\n')
m=int(input('请输入范围最小值'))
n=int(input('请输入范围最大值'))
print('%s-%s猜数字\n'%(m,n))
a=int(input('请输入:'))
b=random.randint(m,n)
#print(b)

i=1
while a!=b:
    i+=1
    if a>b:
        print('大了大了')
        a=int(input('不对,再猜一次:'))
    elif a<b:
        print('小了小了')
        a=int(input('不对,再猜一次:'))
print('居然被你蒙对了!\n')

print('游戏结束,总共猜了%d次'%i)
