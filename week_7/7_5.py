# Initialize an accumulator variable.
total = 0.0

# 0 SENTINEL

number= int(input("Enter a number,enter 0 to quit  "))

while number!= 0:
    total = total + number
    number= int(input("Enter a number:,enter 0 to quit  " ))

# Display the total of the numbers.
print('The total is', total)