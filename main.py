import random
def guess_game():
    n = random.randint(1,100)

    a = 0
    guesses = 1
    print("\n🎮 Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100:\n")


    while(n != a):

        a = int(input("👉 Guess The Number: "))
        if (n > a):
            print("📈 Higher Number Please!")
            guesses += 1
        elif(n<a):
            print("📉 Lower Number Please!")
            guesses += 1
    print(f"\n✅ You guessed the number {n} correctly in {guesses} attempts!")

    try:
        with open("hiscore.txt","r") as f:
            hiscore = f.read()
            if(hiscore != ""):
                hiscore = int(hiscore)
    except FileNotFoundError:
        hiscore = 0

    if hiscore == 0 or guesses<hiscore:
        print("🏆 New High Score! Congratulations!\n")
        with open("hiscore.txt","w") as f:
            f.write(str(guesses))
    else:
        print(f"📌 Current High Score: {hiscore} attempts.\n")
while True:
    guess_game()
    again =input("🔁 Do you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("\n👋 Thanks for playing! See you next time.")
        break


