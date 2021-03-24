#BU PROGRAM İSİM VE HAL HATIR SORAR

isim = input("Isminiz nedir? ")
print("Merhaba",isim,"nasilsin?")


fiyat=int(input("Urünün fiyati nedir "))
indirim=fiyat*0.2  #yüzde 20si
yenifiyat=fiyat-indirim
print("Indirimli fiyat",yenifiyat)


test1=int(input("Birinci sinav sonucu "))
test2=int(input("Ikinci sinav sonucu "))
test3=int(input("Ucüncü sinav sonucu "))
ort=(test1+test2+test3)/3
print("Ortalamanız",ort,"Puan")


girilen = int(input("Enter seconds "))
hours= girilen // 3600
mins = (girilen - (hours*3600)) // 60
secs=girilen-(hours*3600)-(mins*60)
print("Hours:",hours,"minutes:",mins,"seconds:",secs)

