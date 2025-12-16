import random
layout=[[' ','|',' ','|',' '],['-','+','-','+','-'],[' ','|',' ','|',' '],['-','+','-','+','-'],[' ','|',' ','|',' ']]
for x in layout:
    print(' '.join(x))
choice_list=[]
playerchoice_list=[]
computerchoice_list=[]
count=0
win=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]


def check_winner():
    for combo in win:
        if all(v in playerchoice_list for v in combo):
            print("Player wins!")
            return True
        if all(v in computerchoice_list for v in combo):
            print("Computer wins!")
            return True
    return False


while count<=9:
    playerchoice=int(input('Enter your move(1 to 9):'))
    if playerchoice in choice_list:
        print("ERROR\nAlready someone has chosen that spot")
        break
    else:
        if playerchoice<=3:
            if playerchoice==1:
                row=layout[0]
                row[0]='X'
                layout[0]=row
                count+=1
                choice_list.append(playerchoice)
                playerchoice_list.append(playerchoice)
                for x in layout:
                    print(' '.join(x))
            elif playerchoice==2:
                row=layout[0]
                row[2]='X'
                layout[0]=row
                count+=1
                choice_list.append(playerchoice)
                playerchoice_list.append(playerchoice)
                for x in layout:
                    print(' '.join(x))
            elif playerchoice==3:
                row=layout[0]
                row[4]='X'
                layout[0]=row
                count+=1
                choice_list.append(playerchoice)
                playerchoice_list.append(playerchoice)
                for x in layout:
                    print(' '.join(x))
            

        elif playerchoice>3 and playerchoice<=6:
            if playerchoice==4:
                row=layout[2]
                row[0]='X'
                layout[2]=row
                count+=1
                choice_list.append(playerchoice)
                playerchoice_list.append(playerchoice)
                for x in layout:
                    print(' '.join(x))
            elif playerchoice==5:
                row=layout[2]
                row[2]='X'
                layout[2]=row
                count+=1
                choice_list.append(playerchoice)
                playerchoice_list.append(playerchoice)
                for x in layout:
                    print(' '.join(x))
            elif playerchoice==6:
                row=layout[2]
                row[4]='X'
                layout[2]=row
                count+=1
                choice_list.append(playerchoice)
                playerchoice_list.append(playerchoice)
                for x in layout:
                    print(' '.join(x))

        elif playerchoice>6 and playerchoice<=9:
            if playerchoice==7:
                row=layout[4]
                row[0]='X'
                layout[4]=row
                count+=1
                choice_list.append(playerchoice)
                playerchoice_list.append(playerchoice)
                for x in layout:
                    print(' '.join(x))
            elif playerchoice==8:
                row=layout[4]
                row[2]='X'
                layout[4]=row
                count+=1
                choice_list.append(playerchoice)
                playerchoice_list.append(playerchoice)
                for x in layout:
                    print(' '.join(x))
            elif playerchoice==9:
                row=layout[4]
                row[4]='X'
                layout[4]=row
                count+=1
                choice_list.append(playerchoice)
                playerchoice_list.append(playerchoice)
                for x in layout:
                    print(' '.join(x))

    if check_winner():
        break
        
    
    print('-----------------------------------')

    
    conflict=True
    while conflict==True:
        computerchoice=random.randrange(1,10)
        if computerchoice in choice_list:
            conflict=True
            continue
        else:
            conflict=False
            if computerchoice<=3:
                if computerchoice==1:
                    row=layout[0]
                    row[0]='O'
                    layout[0]=row
                    count+=1
                    choice_list.append(computerchoice)
                    computerchoice_list.append(computerchoice)
                    for x in layout:
                        print(' '.join(x))
                elif computerchoice==2:
                    row=layout[0]
                    row[2]='O'
                    layout[0]=row
                    count+=1
                    computerchoice_list.append(computerchoice)
                    choice_list.append(computerchoice)
                    for x in layout:
                        print(' '.join(x))
                elif computerchoice==3:
                    row=layout[0]
                    row[4]='O'
                    layout[0]=row
                    count+=1
                    choice_list.append(computerchoice)
                    computerchoice_list.append(computerchoice)
                    for x in layout:
                        print(' '.join(x))
                
        
            elif computerchoice>3 and computerchoice<=6:
                if computerchoice==4:
                    row=layout[2]
                    row[0]='O'
                    layout[2]=row
                    count+=1
                    choice_list.append(computerchoice)
                    computerchoice_list.append(computerchoice)
                    for x in layout:
                        print(' '.join(x))
                elif computerchoice==5:
                    row=layout[2]
                    row[2]='O'
                    layout[2]=row
                    count+=1
                    choice_list.append(computerchoice)
                    computerchoice_list.append(computerchoice)
                    for x in layout:
                        print(' '.join(x))
                elif computerchoice==6:
                    row=layout[2]
                    row[4]='O'
                    layout[2]=row
                    count+=1
                    choice_list.append(computerchoice)
                    computerchoice_list.append(computerchoice)
                    for x in layout:
                        print(' '.join(x))

            elif computerchoice>6 and computerchoice<=9:
                if computerchoice==7:
                    row=layout[4]
                    row[0]='O'
                    layout[4]=row
                    count+=1
                    choice_list.append(computerchoice)
                    computerchoice_list.append(computerchoice)
                    for x in layout:
                        print(' '.join(x))
                elif computerchoice==8:
                    row=layout[4]
                    row[2]='O'
                    layout[4]=row
                    count+=1
                    choice_list.append(computerchoice)
                    computerchoice_list.append(computerchoice)
                    for x in layout:
                        print(' '.join(x))
                elif computerchoice==9:
                    row=layout[4]
                    row[4]='O'
                    layout[4]=row
                    count+=1
                    choice_list.append(computerchoice)
                    computerchoice_list.append(computerchoice)
                    for x in layout:
                        print(' '.join(x))
    
    if check_winner():
        break