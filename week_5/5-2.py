hours = int(input("How many hours has the employee worked? "))
hourlyrate = float(input("Enter hourly rate: "))

if hours>40:
    wage = hourlyrate*40
    overtime = (hours-40) * hourlyrate * 1.5
    print("Total with overtime: ",wage,"+",overtime,"=",wage+overtime)

else:
    wage=hourlyrate*hours
    print("Total wage :",wage)