import random

# sets up i for while loop & the special number that
# the user has to guess
i = 0
special_Number = random.randint(0, 101)
special_Number = int(special_Number)

# used for testing purposes if this was an actual game than this wouldn't be there
print(special_Number)
# sets up while loop
while(i < 10):

    i = i + 1
    # makes user guess a number
    user_Guess = int(input("Guess a # btw 1 & 100 - make sure to enter an integer "))

    # gives user useful but highly critical hints
    if (user_Guess != special_Number):

        # tests if user is higher than the special number and gives them a hint
        if(user_Guess > special_Number):
            print("you're too high sped ")

        # tests if user is lower than the special number and gives them a hint
        if(user_Guess < special_Number):
            print("you're too low sped ")

    # checks if user guesses the right number
    if (user_Guess == special_Number):
        
        # the user wins if they guess the right number
        print("You won - wooohooo :)")
        number_Of_Guesses = i
        print("It took you " + str(number_Of_Guesses) + " try(- y and add ies) to guess the number gj, well done, exceptional work")
        i = 11
        
    if(i == 10):
        print("You lost :( big sad")

