import random

def guessing_game():
    print("WELCOME TO THE GAME OF GUESSING THE NUMBERS!                                                        ATTEMPTS REMAINING : 5")

    while True:
        attempts = 5
        num = random.randint(1, 10)
        print(f"\nI'm thinking of a number between 1 and 10. You have {attempts} attempts.\n")

        user = int(input("GUESS THE NUMBER: "))

        while num != user:
            if user > num:
                print("It is higher than the number.")
            else:
                print("It is lower than the number.")

            attempts -= 1
            if attempts == 0:
                print(f"You lost! The number was {num}.")
                break

            print(f"                                                                                         ATTEMPTS REMAINING: {attempts}")
            user = int(input("GUESS THE NUMBER: "))

        else:
            print("You won!")
            print("Congratulations! You guessed the number!")

        ask = input("\nDo you want to play again? (y/n): ")
        if ask.lower() != "y":
            break

    print("Thank you for playing!")

# 👉 Start the game!
guessing_game()