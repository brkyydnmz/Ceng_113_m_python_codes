import math

kisi = int(input("How many people? "))
kisidog = int(input("How many hotdogs per person? "))

#calculate number of hotdogs we need
totaldogs = kisi*kisidog

paketdogs = math.ceil(totaldogs/10)  # math.ceil 2.5 paket ise misal 3 yapıyor yukarıya yuvarlar
paketbuns = math.ceil(totaldogs/8)

print("You will need",totaldogs,"hotdogs")
print("You will need",paketdogs,"packages of hotdogs")
print("You will need",paketbuns,"packages of buns")