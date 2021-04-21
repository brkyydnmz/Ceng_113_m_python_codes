hiz=int(input("Hangi hızda gidiyorsun? "))
sure = int(input("Kac saat gideceksin? "))

print("Saat \t mesafe")
for i in range (1,sure+1):
    print(i,'\t',i*hiz)
