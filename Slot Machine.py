import random
import time

def spin():
    symbols = ["🍒", "🍋", "🍉", "💎", "7️⃣"]
    return [random.choice(symbols) for _ in range(3)]

def print_slots(slots):
    print(" | ".join(slots))

def slot_machine():
    balance = 100
    print("🎰 Welcome to the Python Slot Machine!")
    print("💰 You start with 100 coins.")
    print("Each spin costs 10 coins. Matching 3 symbols = you win!")
    print("-" * 40)

    while balance >= 10:
        choice = input("\nPress Enter to spin (or type 'q' to quit): ").lower()
        if choice == 'q':
            break

        balance -= 10
        print("\nSpinning...", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print("\n")

        slots = spin()
        print_slots(slots)

        
        if slots[0] == slots[1] == slots[2]:
            if slots[0] == "7️⃣":
                win = 100
                print("🎉 JACKPOT! You got triple 7️⃣! +100 coins!")
            else:
                win = 50
                print(f"🍀 You matched three {slots[0]}! +50 coins!")
            balance += win
        elif slots[0] == slots[1] or slots[1] == slots[2] or slots[0] == slots[2]:
            win = 20
            balance += win
            print("✨ Two symbols match! +20 coins!")
        else:
            print("😞 No match this time!")

        print(f"💰 Current Balance: {balance} coins")

    print("\n🏁 Game Over! Final Balance:", balance)
    print("Thanks for playing! 🎲")

slot_machine()
