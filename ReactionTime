import random, time, os, csv

print("--Reaction Time Test--")
print("Press the correct letter (A–Z) as fast as you can when the message is shown.\n")

score_file = "Best_Times.csv"
Top_Times = []

if os.path.exists(score_file):
    with open(score_file, "r") as scorefile:
        reader = csv.reader(scorefile)
        for row in reader:
            if row:
                Top_Times.append(float(row[0]))


# Main game code
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

    Top_Times.append(result)
    Top_Times.sort()
    Top_Times = Top_Times[:5]

    with open(score_file, "w", newline="") as scorefile:
        writer = csv.writer(scorefile)
        for s in Top_Times:
            writer.writerow([s])

    print('-' * 25)
    print("\nYour Top 5 Fastest Times:")
    rank = 1
    for t in Top_Times:
        print(rank, ":", round(t, 3))
        rank += 1
    print()

    play = input("Try again? (y/n): ").lower()
    if play != "y":
        print("Okay, bye!")
        break

else:
    print('Bye!')
