def main():
    print("*****Grade Number Calculator*****")
    average_number=calc_average()
    determine_grade(average_number)
    print(input("Letter Grade was calculated.Please press Enter and close."))

def calc_average():
    total=0
    
    for i in range(1,6):
        a=int(input("What is your score? ")) 
        total=total+a
    print("Sum of 5 scores:",total)
    average_number = (total)/5
    print("!!!!! Your average number is ",format(average_number,'2.2F'),"!!!!!")
    return average_number

def determine_grade(average_number):
    if average_number>=90 and average_number<=100:
        print("Your Letter Grade is A")
    if average_number>=80 and average_number<=89:
        print("Your Letter Grade is B")
    if average_number>=70 and average_number<=79:
        print("Your Letter Grade is C")
    if average_number>=60 and average_number<=69:
        print("Your Letter Grade is D")
    if average_number<60:
        print("Your Letter Grade is F")

main()