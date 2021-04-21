#8. Average Word Length
#Write a program with a loop that repeatedly asks the user to enter a word. The user should
#enter nothing (press Enter without typing anything) to signal the end of the loop. Once the
#loop ends, the program should display the average length of the words entered, rounded to
#the nearest whole number.

kelime = input("Bie kelime giriniz.Bos enter ile bitirin.")
print(len(kelime))

totuzun=0
totkelime=0

while kelime != "": #kelime boş olmadığı müddetçe
    uzunluk = len(kelime)
    totuzun += uzunluk 
    totkelime +=1 
    kelime = input("Bir kelime giriniz.Bos enter ile bitirin.")

print("Ortalama uzunuluk:",totuzun/totkelime)