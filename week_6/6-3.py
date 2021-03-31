#Quantity Discount
#10–19 10%
#20–49 20%
#50–99 30%
#100 or more 40%

birimfiyat = 99

adet= int(input("Kac tane almak istersiniz? "))

if adet<10:
    indirim=0
elif adet<20:
    indirim=10
elif adet<50:
    indirim=20
elif adet<100:
    indirim=30
else:
    indirim=40

toplam=birimfiyat*adet
indirimtoplam=toplam/100*indirim
geneltop = toplam-indirimtoplam
print("Toplam: ",toplam)
print("Indirim yuzdesi: ",indirim)
print("Indirim toplam: ",indirimtoplam)
print("Odemeniz gereken miktar: ",geneltop)
