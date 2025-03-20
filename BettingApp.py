import random

def betting_App():
    print("Welcome to the Betting App")
    print("You can bet on a number between 1 and 10")
    print("If you win, you will get 2 times your bet amount")
    print("If you lose, you will lose your bet amount")

    bet = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            bet_amount = int(input("Enter your bet amount: "))
            bet_number = int(input("Enter your bet number: "))
            attempts += 1
            if bet_number == bet:
                print("Congratulations! You have won the bet")
                print("You have won", bet_amount * 2)
                print("Number of attempts:", attempts)
                
            else:
                print("Sorry! You have lost the bet")
                print("You have lost", bet_amount)
                print("Number of attempts:", attempts)

                break

        except ValueError:
                
                print("Please enter a valid number")

betting_App()            
