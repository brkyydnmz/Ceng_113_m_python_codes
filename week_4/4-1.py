# P = F /(1+r)n
# P = Present value
# F = Future value
# r = annual interest rate
# n = years


F = float(input("Enter desired future amount "))
r = float(input("Enter yearly interest rate "))
n = int(input("How many years ? "))

P = F / (1+r)**n

print("Then you must deposit ",P,"now")

