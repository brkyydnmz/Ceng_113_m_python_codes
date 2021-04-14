#2. Calories Burned
#Running on a particular treadmill you burn 4.2 calories per minute. Write a program that
#uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.

for mins in range(10,31,5):
    print("mins=",mins,"  calories=",mins*4.2)