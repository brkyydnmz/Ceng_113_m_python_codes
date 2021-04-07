sinavsayisi=0
sinavtoplami=0

print("Sınav sonucunu yazın,-1 ile çıkın")
sinav=float(input("Sınav sonucu:"))
while sinav <-1 or sinav > 100:
    print("Error try again")
    sinav=float(input("Sınav sonucu:"))

while sinav != -1:
    sinavtoplami += sinav
    sinavsayisi += 1
    sinav=float(input("Sınav sonucu:"))
    while sinav <-1 or sinav > 100:
        print("Error try again")
        sinav=float(input("Sınav sonucu:"))

print("Ortalaması:", sinavtoplami/sinavsayisi)