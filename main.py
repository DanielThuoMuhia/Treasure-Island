print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice_input = input('You are at a crossroad, where do you want to go "left" or "right".').lower()


if choice_input == "left":
    choice_2 = input('You are approaching a lake. There is an island in the middle of the lake. '
                     'Type "Wait" to wait for a boat. Type "Swim" to swim across.').lower()
    if choice_2 == "Wait":
        choice_3 = input("You arrived at the island unharmed. "
                         "There is a house with 3 doors. One red, One yellow and one blue. "
                         "Which color do you choose?").lower()
        if choice_3 == "red":
            print("Its a room full of fire game over.")
        elif choice_3 == "yellow":
            print("You found the treasure you win")
        elif choice_3 == "blue":
            print("you have entered a room full of beast. Game Over.")
        else:
            print("You chose a door that doesnt exist. Game Over.")
    else:
        print("You got attacked by a crocodile, Game Over")
else:
    print("Game Over.")


