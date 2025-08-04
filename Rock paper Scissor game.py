import random
i=1
game_image=['✊','🖐️','✌️']
while i<=3 :
    user=int(input("Enter your choose 0.Rock , 1.Paper and 2.Scissor : "))
    print(f'Your choose {game_image[user]}')
    computer=random.randint(0,2)
    print(f'Computer choose {game_image[computer]}')
    if user==computer :
        print('< Draw >')
    elif user==0 and computer==1 :
     print(">> Computer Winner")
    elif user==0 and computer==2 :
     print(">> User Winner")
    elif user==1 and computer==0 :
        print(">> User Winner")
    elif user==1 and computer==2 :
        print(">> Computer Winner")
    elif user==2 and computer==0 :
        print(">> Computer Winner")
    elif user==2 and computer==1 :
        print(">> User Winner")
    else:
        print('Enter correct choose')
    print()
    i+=1
