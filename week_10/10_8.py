import random

mynum= random.randint(1,100)
print("I am thinking of a number from 1 to 100")

guess = int(input("Enter your guess:"))

while ( guess != mynum):
    if(mynum>guess):
        print("Your guess is too low...")
    else:
        print("Your guess is too high..")
    guess = int(input("Enter your guess:"))

print("Congratulations! I was guessing",mynum,"indeed!")