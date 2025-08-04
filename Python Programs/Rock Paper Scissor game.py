import random
i=1 
get_emoji=['✊','🖐️','✌️']
while i<=3 :                    # iterate while loop over 3 times
    user=int(input("Enter your choose 0.Rock , 1.Paper and 2.Scissor : "))     
    print(f'Your choose {get_emoji[user]}')# get emoji based on the number that entered by the User
    computer=random.randint(0,2)                    # taking random number 0 to 2
    print(f'Computer choose {get_emoji[computer]}') # get emoji based on the random number
    if user==computer :
        print('< Draw >')
    elif user==0 and computer==1 :     # User->rock & Computer->Paper
     print(">> Computer Winner")
    elif user==0 and computer==2 :     # User->rock & Computer->Paper
     print(">> User Winner")
    elif user==1 and computer==0 :     # User->Paper & Computer->Rock
        print(">> User Winner")
    elif user==1 and computer==2 :     # User->Paper & Computer->Scissor
        print(">> Computer Winner")
    elif user==2 and computer==0 :     # User->Scissor & Computer->Rock
        print(">> Computer Winner")
    elif user==2 and computer==1 :     # User->Scissor & Computer->Paper
        print(">> User Winner")
    else:
        print('Enter correct choose') # printing a message when invalid input is given
    print()
    i+=1
