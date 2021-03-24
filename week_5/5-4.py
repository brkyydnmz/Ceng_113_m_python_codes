score = int(input("Enter score: "))

#1.yol
if score >=90:
    print("A")
if score>=80 and score<=89:
    print("B")
if score>=70 and score <=79:
    print("C")
if score>=60 and score<=69:
    print("D")
if score<60:
    print("F")


#2.yol
if score >= 90:
    print("A")
else:
    if score>=80:
        print("B")
    else:
        if score>=70:
            print("C")
        else:
            if score>=60:
                print("D")
            else:
                print("F")
