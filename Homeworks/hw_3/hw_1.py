def main():
    kilometers=float(input("What is your distance in kilometers? "))
    print("Your kilometers is:",kilometers)

    miles = kilometers*0.6214
    print("We converted your kilometers to miles.")
    print("Your result is:",format(miles,'4.4F'),"miles",)
    print(input("Result was calculated.Please press Enter and close."))

main()