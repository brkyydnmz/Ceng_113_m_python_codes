# Create a global variable.
number = 0

def main():
    global number #globaldeki number ı değiştirmek için başına global yazdık
    number = int(input('Enter a number: '))
    show_number()

def show_number():
    print('The number you entered is', number)

# Call the main function.
main()
