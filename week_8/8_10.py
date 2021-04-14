#10. Tuition Increase
#At one college, the tuition for a full-time student is $8,000 per semester. It has been announced
#that the tuition will increase by 3 percent each year for the next 5 years. Write a program
#with a loop that displays the projected semester tuition amount for the next 5 years.

tuit = 8000
for years in range(1,6):
    tuit = tuit + (tuit/100*3)  #tuit+= tuit/100*3
    print("year:",years,"tuition: $",format(tuit,",.2f"))