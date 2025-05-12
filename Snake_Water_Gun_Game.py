#Snake , water ,  gun game 
print ("Welcome to the Snake, Water, Gun game".center(50, "-"))

def snake_water_gun():
    import random
    # Taking input from the user    
    print("Please enter your choice:".center(50, "-"))
    print("1. Snake")
    print("2. Water")
    print("3. Gun")
    print("4. Exit")

    choice = int(input("Enter your choice (1/2/3): "))
    if choice == 1:
        user = "Snake"
    elif choice == 2:
        user = "Water"
    elif choice == 3:
        user = "Gun"
    elif choice == 4:
       print("Exitting the game ...".center(50, "-"))
       exit()
    else:
        print("Invalid choice! Please try again.")
        snake_water_gun()
        return  

    # Generating a random choice for the computer
    computer = random.choice(["Snake", "Water", "Gun"])
    print("Computer choice: ", computer)

    #Displaying the choices
    print("Your choice: ", user)
    print("Computer choice: ", computer)

    #Determining the winnner 
    if(user.lower() == computer.lower()):
        print("It's a tie!")
    elif((user.lower() == "snake" and computer.lower() == "water") or (user.lower() == "water" and computer.lower() == "gun") or (user.lower() == "gun" and computer.lower() == "snake")):
       print("You win!")
    elif((user.lower() == "water" and computer.lower() == "snake") or (user.lower() == "gun" and computer.lower() == "water") or (user.lower() == "snake" and computer.lower() == "gun")):
        print("You loose!")



snake_water_gun()
while True:
    # Asking the user if they want to play again
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "y":
        print("Restarting the game ...".center(50, "-"))
        # Restart the game
        snake_water_gun()
    
    elif play_again == "n":
        print("Exitting the game ...".center(50, "-"))
        exit()