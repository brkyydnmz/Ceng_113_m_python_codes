def main():
    print("Welcome to the sports club diet assessment center. Enter your gram of fat and gram of carbohydrate respectively.")
    fat_gram=float(input("What is number of your consumed fat gram in a day? "))
    calories_from_fat=fat_gram*9
    print("Number of calories that result from the fat:",format(calories_from_fat,'2.2F'),"calories")

    carbohydrate_gram=float(input("What is number of your consumed carbohydrate gram in a day? "))
    calories_from_carbs=carbohydrate_gram*4
    print("Number of calories that result from the carbohydrate:",format(calories_from_carbs,'2.2F'),"calories")

    total_calories= calories_from_fat + calories_from_carbs
    print("Your total result of calories:",total_calories)
    
    print(input("Results were calculated.Please press Enter and close."))
main()