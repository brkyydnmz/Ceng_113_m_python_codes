import turtle 
turtle.forward(200)  #ekranda 200 birim ileri
turtle.left(90) #turtle 90 derece döndü
turtle.forward(200)
turtle.right(120) #120 derece sağa
turtle.forward(120)
turtle.pensize(10) #kalem kalınlıgı
turtle.pencolor('red') #renk kırmızıya döndü
turtle.begin_fill() #içini doldurur
turtle.circle(110) #110 capında daire olur
turtle.end_fill() #içi doldurulcak alanı bitir
turtle.write('bitti')

print(input("a"))