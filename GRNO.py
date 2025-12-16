import random
choice=input('Press y to run the game: ')
if choice.lower()=='y':
    playerchoice=True
    i=int(input('Enter the number of rounds:'))
else:
    playerchoice=False
pno2_win=0
pno1_win=0
while playerchoice==True:
    tie=0
    for x in range(0,i):
        if x<i: 
            pno1=random.randrange(1,6)
            pno2=random.randrange(1,6)
            if pno1>pno2:
                print("PLAYER 1 WINS ")
                pno1_win+=1
            elif pno1==pno2:
                print('TIE')
                tie+=1
            else:
                print("Player 2 WINS ")
                pno2_win+=1
        elif x>=i:
            playerchoice=False

final_score=pno1_win-pno2_win
print('SCORE:')
print('No. of times player 1 won:',pno1_win)
print('No. of times player 2 won:',pno2_win)
print('No. of ties:',tie)
if final_score>0:
    print("PLAYER 1 wins by", final_score)
else:
    print('PLAYER 2 wins by', final_score)
print('')
print('Thank you for playing')

playerchoice=False
