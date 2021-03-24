print("Hello")  #string character
# WRONG!!!  print("ilk programımız "merhaba" oldu")
print("ilk program 'merhaba' oldu")
print('ilk program "Merhaba" oldu')

age=27  #variable
print(age)

age2=35+10
print(age2)
print("benim yasim: ",age2)

isim="Berkay"
print("Ismim:",isim)
print("Ismim de "+ isim)  #for string use +
print("Ismim:",isim,"Yas:",age)

isim="Ahmet"
print("isim simdi",isim,"oldu")

age= age+ 10  #27+10 =37
print("10 sene sonra yasim",age,"olacak")

age=int(input("Yasiniz kac? ")) #input integer değer olacak
print("Yasiniz",age,"o zaman...\n")  # \n boş satır bıraktırmayı sağlar

onsene = age+10   #age input değerdi string yani onun üstüne integer ekleme yapamayız  #başına int koyduk inputun integer değerler gelebildi
print("On sene sonra",onsene,"yasinda olacaksiniz")

age=float(input("Yasiniz kac? ")) #input float(ondalıklı değer) değer olacak
print("Yasiniz",age,"o zaman...\n")  # \n boş satır bıraktırmayı sağlar

degisken=int(88.23232)
print(degisken)
print(degisken+9.7372)  #float a döndü integer

ikinci=float(188)
print(ikinci)
print(type(ikinci))   #type değişken tipini söyler


