#Determine whether the year is divisible by 100. 
# If it is, then it is a leap year if and only
#if it is also divisible by 400. For example, 2000 is a leap year, but 2100 is not.
#2. If the year is not divisible by 100, then it is a leap year if and only if it is divisible by 4.
#For example, 2008 is a leap year, but 2009 is not.

year= int(input("Enter year "))

if(year%100 == 0):
    if(year %400 == 0):
        print("Leap year!")
elif (year%4 == 0):
    print("Leap year!!")
else:
    print("NOT a leap year")