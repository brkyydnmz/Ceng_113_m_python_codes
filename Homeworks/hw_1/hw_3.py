#Using integer writing this project.
#When we use a float number, it finds many numbers after the comma.
print("***Percentage of man and woman***")
men=int(input("Number of men:"))
women=int(input("Number of women:"))
total= men + women

permen= (men/total)*100
perwomen= (women/total)*100

print("Percentage of men:",int(permen))
print("Percentage of women:",int(perwomen))

