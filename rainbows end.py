
'''
Problem 7:
The theme park Rainbow's End has a list of person specifications for each ride. Some
of these are listed below. Using the information below, design and write a program
which will ask for a person's height and age and present them with a list of rides they
are eligible to ride on.
'''

# Variables

# Attractions for those 9 and under
nine_and_under = ["Dragon Flight Coaster", "Freddo’s Aeroplane Ride","Car Wash Convoy",
"Bouncy Castle – children must be 100cm or under","Jumpin’ Star – children must be at least 90cm"]

# Attractions for those 80cm and up
user_80cm_and_up = ["Goldrush – a responsible person must accompany those under 100cm",
"Log Flume – a responsible person must accompany those under 100cm",
"Pirate Ship – a responsible person must accompany those under 100cm",
"Dodgems – as passenger only, a responsible person must accompany those under 120cm",
"Family Karts – as passenger only, a responsible person must accompany those under 150cm"]

# Attractions for those 120cm and up
user_120cm_and_up = ["FearFall – maximum height 195cm","Corkscrew Coaster",
"Bumper Boats","Dodgems","Invader"]

# Attractions for those 150cm and up
user_150cm_and_up = ["Scorpion Karts", "Family Karts"]

# Attractions for all
attractions_for_all = ["Mini Golf","Cinema 180"]

user_age = 0
user_height = 0
CONTINUE_ATTRIBUTE_LOOP = True
CONTINUE_REDO_LOOP = True

# Functions

def attractions_for_you():

    if user_age <= 9:
        # For every element in the list it prints out each element in order
        for attraction in range(len(nine_and_under)):
            print(nine_and_under[attraction])
    if user_height >= 80:
        # "
        for attraction in range(len(user_80cm_and_up)):
            print(user_80cm_and_up[attraction])
    if user_height >= 120:
        # "
        for attraction in range(len(user_120cm_and_up)):
            print(user_120cm_and_up[attraction])
    if user_height >= 150:
        # "
        for attraction in range(len(user_150cm_and_up)):
            print(user_150cm_and_up[attraction])
    if user_height > 0 and user_age > 0:
        # "
        for attraction in range(len(attractions_for_all)):
            print(attractions_for_all[attraction])

# Main routine

while CONTINUE_ATTRIBUTE_LOOP == True:
    while user_age  < 1:
        try:
            user_age = int(input("\nPlease enter your age.\n>>> "))
        except ValueError:
            # Catches any "Value Errors" made and instead prints out "That is not a valid age"
            print("\nThat is not a valid age\n")

    while user_height < 1:
        try:
            user_height = int(input("\nPlease enter your height.\n>>> "))
        except ValueError:
            # Catches any "Value Errors" made and instead prints out "That is not a valid height"
            print("\nThat is not a valid height\n")

    attractions_for_you()

    # If I don't reset the constant then it will infinitely loop a given list
    CONTINUE_REDO_LOOP = True
    while CONTINUE_REDO_LOOP == True:
        # The program will know if the user has already entered an age and height in if they're greater than 0
        if user_age > 0 and user_height > 0:
            redo_proccess = input("\nWould you like to find the ride for another height group?\nAnswer yes or no\n>>> ")
            if redo_proccess.lower() == "yes":
                # Resets the age and height because if I didn't it would ignore the while loops with the age/height input
                # This is because the user age is greater than < 1
                # Could store previous age's and heights in a list if they didn't want their data lost
                user_age = 0
                user_height = 0
                # Changing this constant to false breaks the user out of ONLY this loop
                CONTINUE_REDO_LOOP = False
            elif redo_proccess.lower() == "no":
                # If the user doesn't wish to continue they will be broken out of both loops
                CONTINUE_ATTRIBUTE_LOOP = False
                CONTINUE_REDO_LOOP = False
            else:
                # If anything but yes or no is given, the user will recieve this message and be put through the loop again
                print("\nThat is not a proper answer")

print("\nThank you, Goodbye!")


