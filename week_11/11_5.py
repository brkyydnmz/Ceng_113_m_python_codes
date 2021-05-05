def is_even(num):
    return(num%2==0)

t = int(input("Enter number"))

blurb='odd'
if(is_even(t)):
    blurb='even'

print("That number is "+blurb)

