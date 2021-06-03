print("Welcome to my max function.Please input numbers.Just integer numbers!!")

number1=int(input("What is your First number? "))
number2=int(input("What is your Secon number? "))

def max():
    if number1>number2:
        print("Your max number is ",number1)
    if number2>number1:
        print("Your max number is ",number2)
    if number1==number2:
        print("Your numbers are equal")
    
    print(input("Finished max function.Please press Enter and close."))

max()
