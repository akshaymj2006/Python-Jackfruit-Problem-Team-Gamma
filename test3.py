import random
import time
import os
import csv 

print("Welcome to our Ultimate Arcade!")
print("Every Player Starts with 100 Coins. First Player to reach 500 Coins Wins!")

acc1 = 100
acc2 = 100

def spin():
    
    print("Spinning the slot machine...")
    time.sleep(5)
    balance_change = 0
    symbols = ["🍒", "🍋", "🍉", "💎", "7️⃣"]
    slots = [random.choice(symbols) for _ in range(3)]
    
    print(" | ".join(slots))
    if slots[0] == slots[1] == slots[2]:
        if slots[0] == "7️⃣":
            win = 100
            print("🎉 JACKPOT! triple 7️⃣! +100 coins!")
        else:
            win = 50
            print(f"🍀 You matched three {slots[0]}! +50 coins!")
        balance_change += win
    else:
        print("No match.")
    return balance_change

def reactiontime_test():
    score_file = "Best_Times.csv"
    Top_Times = []

    if os.path.exists(score_file):
        with open(score_file, "r") as scorefile:
            reader = csv.reader(scorefile)
            for row in reader:
                if row:
                    Top_Times.append(float(row[0]))

    coins = 0

    play = input('Are you ready?(y/n): ').lower()
    while play == 'y':
        print("Get ready...")
        time.sleep(random.uniform(1.0, 4.0))

        target = random.choice("abcdefghijklmnopqrstuvwxyz")
        print(f"TYPE THE LETTER: {target.upper()}")

        start = time.perf_counter()

        while True:
            user_input = input().strip().lower()
            if user_input == target:
                end = time.perf_counter()
                break
            print("Wrong letter! Type again:")

        result = end - start
        print("-"*25)
        print("Your time:", round(result, 3), "seconds")

        if result < 0.5:
            coins += 100
        elif result < 1.0:
            coins += 50

        play = input("Try again? (y/n): ").lower()
        if play != "y":
            print("Okay, bye!")
            break
    return coins

def tictactoe():
    layout=[[' ','|',' ','|',' '],
            ['-','+','-','+','-'],
            [' ','|',' ','|',' '],
            ['-','+','-','+','-'],
            [' ','|',' ','|',' ']]

    choice_list=[]
    playerchoice_list=[]
    computerchoice_list=[]
    count=0
    coins = 0

    win=[[1,2,3],[4,5,6],[7,8,9],
         [1,4,7],[2,5,8],[3,6,9],
         [1,5,9],[3,5,7]]

    def print_board():
        for x in layout:
            print(' '.join(x))

    def check_winner():
        nonlocal coins
        for combo in win:
            if all(v in playerchoice_list for v in combo):
                print("Player wins!")
                coins += 100
                return "PLAYER"
            if all(v in computerchoice_list for v in combo):
                print("Computer wins!")
                return "COMPUTER"
        return None

    print_board()

    while count <= 9:
        playerchoice = int(input('Enter your move(1 to 9): '))

        if playerchoice in choice_list:
            print("ERROR\nAlready someone has chosen that spot")
            break

        if playerchoice <= 3:
            row = layout[0]
            idx = (playerchoice-1)*2
            row[idx] = 'X'
            layout[0] = row
        elif playerchoice <= 6:
            row = layout[2]
            idx = (playerchoice-4)*2
            row[idx] = 'X'
            layout[2] = row
        else:
            row = layout[4]
            idx = (playerchoice-7)*2
            row[idx] = 'X'
            layout[4] = row

        count += 1
        choice_list.append(playerchoice)
        playerchoice_list.append(playerchoice)
        print_board()

        winner = check_winner()
        if winner:
            break
        if count >= 9:
            print("Draw!")
            break

        print('-----------------------------------')

        conflict = True
        while conflict:
            computerchoice = random.randrange(1,10)
            if computerchoice in choice_list:
                continue
            conflict = False

        if computerchoice <= 3:
            row = layout[0]
            idx = (computerchoice-1)*2
            row[idx] = 'O'
            layout[0] = row
        elif computerchoice <= 6:
            row = layout[2]
            idx = (computerchoice-4)*2
            row[idx] = 'O'
            layout[2] = row
        else:
            row = layout[4]
            idx = (computerchoice-7)*2
            row[idx] = 'O'
            layout[4] = row

        count += 1
        choice_list.append(computerchoice)
        computerchoice_list.append(computerchoice)
        print("Computer chose:", computerchoice)
        print_board()

        winner = check_winner()
        if winner:
            break

    print("Game over.")
    print("You earned:", coins, "coins in Tic Tac Toe")
    return coins

def grno():
    choice = input('Press y to run the game: ')
    if choice.lower() == 'y':
        playerchoice = True
        i = int(input('Enter the number of rounds: '))
    else:
        playerchoice = False

    pno2_win = 0
    pno1_win = 0
    tie = 0

    while playerchoice:
        for x in range(i):
            pno1 = random.randrange(1,6)
            pno2 = random.randrange(1,6)
            if pno1 > pno2:
                print("PLAYER 1 WINS ")
                pno1_win += 1
            elif pno1 == pno2:
                print('TIE')
                tie += 1
            else:
                print("Player 2 WINS ")
                pno2_win += 1
        playerchoice = False

    final_score = pno1_win - pno2_win
    print('SCORE:')
    print('No. of times player 1 won:', pno1_win)
    print('No. of times player 2 won:', pno2_win)
    print('No. of ties:', tie)
    if final_score > 0:
        print("PLAYER 1 wins by", final_score)
    else:
        print('PLAYER 2 wins by', abs(final_score))
    print('Thank you for playing')

    return final_score * 10   # convert to coins

# MAIN ARCADE LOOP
# MAIN ARCADE LOOP
while acc1 < 500 and acc2 < 500:
    print("\nCurrent Coins -> Player 1:", acc1, "| Player 2:", acc2)
    print("COMMON CHOICE FOR BOTH PLAYERS:")
    print("1 for Slot Machine, 2 for Reaction Time Test, 3 for Tic Tac Toe, 4 for Greater Number Game")
    
    common_choice = int(input('Enter the game number to play this round: '))

    # Player 1 turn
    if common_choice == 1:
        acc1 += spin()
    elif common_choice == 2:
        acc1 += reactiontime_test()
    elif common_choice == 3:
        acc1 += tictactoe()
    elif common_choice == 4:
        acc1 += grno()

    # Check after P1 in case they already reached 500
    if acc1 >= 500:
        break

    # Player 2 turn (same game)
    if common_choice == 1:
        acc2 += spin()
    elif common_choice == 2:
        acc2 += reactiontime_test()
    elif common_choice == 3:
        acc2 += tictactoe()
    elif common_choice == 4:
        acc2 += grno()

# Declare winner
if acc1 >= 500:
    print("\nPLAYER 1 WINS THE ULTIMATE ARCADE WITH", acc1, "COINS!")
elif acc2 >= 500:
    print("\nPLAYER 2 WINS THE ULTIMATE ARCADE WITH", acc2, "COINS!")
