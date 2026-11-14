import random

print("Welcome to Rock, Paper, Scissors. You will get unlimited tries to win.")
print("Enter 'R' for Rock, 'P' for Paper, 'S' Scissors: ")


while True:
    randomNumber = (random.randrange(1,4))
    game = input("'Q' to quit. 'B' to begin.")
    if game == "Q":
        print("Goodbye!")
        break
    if game == "B":
        choice = input("Rock, Paper, Scissor? ")
        if choice == "R":
            print("You picked rock")
            if randomNumber == 1:
                print("Computer picked rock. It is a tie.")
            elif randomNumber == 2:
                print("Computer picked paper. You lose.")
            elif randomNumber == 3:
                print("Computer picked scissors. You win.")
            else:
                print("Error")
        elif choice == "P":
            print("You picked paper")
            if randomNumber == 1:
                print("Computer picked rock. You win.")
            elif randomNumber == 2:
                print("Computer picked paper. It is a tie.")
            elif randomNumber == 3:
                print("Computer picked scissors. You lose.")
            else:
                print("Error")
        elif choice == "S":
            print("You picked Scissors")
            if randomNumber == 1:
                print("Computer picked rock. You lose.")
            elif randomNumber == 2:
                print("Computer picked paper. You win.")
            elif randomNumber == 3:
                print("Computer picked scissors. It's a tie.")
            else:
                print("Error")
        else:
            print("Please enter a valid key (R, P, S) ")
    
    