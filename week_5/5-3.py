maas= int(input("Enter yearly wage: "))
years=int(input("How many years at current job: "))

if maas> 30000:
    if years>=2:
        print("You qualify!")
    else:
        print("You need to work at least 2 years")
else:
    print("Your wage must be 30000 at least")