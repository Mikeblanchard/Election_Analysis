# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

if (computer_choice == "r" and user_choice == "r" ):
    print ("Its a tie")

elif (computer_choice == "r"  and user_choice == "s"):
    print ("You lose")

elif (computer_choice == "r" and user_choice == "p"):
    print ("You win")

if (computer_choice == "s" and user_choice == "s" ):
    print ("Its a tie")

elif (computer_choice == "s"  and user_choice == "p"):
    print ("You lose")

elif (computer_choice == "s" and user_choice == "r"):
    print ("You win")


if (computer_choice == "p" and user_choice == "p" ):
    print ("Its a tie")

elif (computer_choice == "p"  and user_choice == "r"):
    print ("You lose")

elif (computer_choice == "p" and user_choice == "s"):
    print ("You win")


# Run Conditionals