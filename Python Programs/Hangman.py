import random
dummy=[]
length=0
itemList=['luffy','zoro','usopp','sanji','jimbe','nami','chopper','frenky','robin','broke']
goal=random.choice(itemList)
for i in goal:
    length+=1
    dummy+='_'
print(dummy)
lives=6
a=True
s=''
while a:

    if lives==0:
        s='+---------------\n|        |\n|        O\n|       /|\ \n|       / \ \n|'
    elif lives==1:
        s='+---------------\n|        |\n|        O\n|       /|\ \n|       /  \n|'
    elif lives==2:
        s='+---------------\n|        |\n|        O\n|       /|\ \n|\n|'
    elif lives==3:
        s='+---------------\n|        |\n|        O\n|       /| \n|\n|'
    elif lives==4:
        s='+---------------\n|        |\n|        O\n|        |\n|\n|'
    elif lives==5:
        s='+---------------\n|        |\n|        O\n|\n|\n|'
    else:
        s='+---------------\n|        |\n|        \n|\n|\n|'
    print(s)
    prediction = input('Enter what do you guess :')
    if prediction in goal:
        for j in range(length):
            if prediction==goal[j]:
                dummy[j]=prediction
        print(dummy)
        print(f'it is Correct you have {lives} chances')
        if dummy==list(goal):
            print('You Win')
            exit()
    else:
        lives-=1
        if lives==0:
            print(' Game Over !')
            exit()
        print(dummy)
        print(f'it is wrong you have  {lives} chances')
