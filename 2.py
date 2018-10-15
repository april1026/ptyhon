import random
max=47
listl=[0 for x in range(8)]
list2=[x for x in range(48)]
for i in range(1,8):
    number=random.randint(1,max)
    listl[i]=list2[number]
    list2[number]=list2[max]
    max-=1
print('您的威力彩號碼是:')
for i in range(1,8):
    if i<7:
        print(listl[i],',',end='')
    else:
        print(listl[i],end='')
number=random.randint(1,6)
print('     特別號:',number)
