test1 = float(input("Enter result of test 1: "))
test2 = float(input("Enter result of test 2: "))
test3 = float(input("Enter result of test 3: "))

goodvalues=True  #varsayılanı true yaptık

if test1 > 100 or test2 > 100 or test3 > 100: # or ile hepsini tekte yazdık
    print("Error in test!")
    goodvalues=False

if goodvalues: #goodlvalues true oldugunda calısır
    #calculate average
    avg= (test1+test2+test3)/3
    print("Your average is:",avg)
    if avg > 95:
        print("Congratulations")
    if avg<30:
        print("So sorry! Better luck next time")