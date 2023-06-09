#Guessing a number game

from random import *

h_number = input("Enter a number : ")
print("Guess a number between 0 to ",h_number)

#checking if the user has entered a number("24") not alphabets("hello")
#So we can apply typecasting of int() on number but not on string

if h_number.isdigit(): 
    h_number = int(h_number)

    if h_number <= 0:
        print("Please enter a number greater than 0!!")
        quit()
else:
    print("Please enter a number not a string!!")
    quit()

random_number = randint(0, h_number)

guess = 0
while True:
    guess += 1
    user_number = input("Guess a number : ")
    if user_number.isdigit():
        user_number = int(user_number)
    else:
        print("Please enter a number not a string!!")
        continue

    if user_number == random_number:
        print("You got it!!")
        break
    elif user_number > random_number:
        print("You are above the number!")
    else:
        print("You are below the number!")

print("You got it in",guess,"guesses.")
