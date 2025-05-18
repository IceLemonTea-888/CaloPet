# A simple calculation of the total calories
# simple_calculation.py


def calculate_total_calories(first_food, food_calorie_table , pet_name ):
    total_calories = 0

    if first_food in food_calorie_table:
        total_calories += food_calorie_table[first_food.lower()]
        print(f"🐱{pet_name}: {first_food}'s is {food_calorie_table[first_food]} calories.")
        
        print(f"\n(🐱{pet_name}:Type 'no' to finish)")
    else:
        print(f"🐱{pet_name}: Sorry! Your food doesn't seem very common :)")

    while True:
        food = input(f"\n🐱 {pet_name}:Anything else? 🐾 ").lower()

        if food == "no":
            break
        elif food in food_calorie_table:
            total_calories += food_calorie_table[food]
            print(f" 🐸{pet_name}: {food}'s calorie is {food_calorie_table[food]} calories.")
            
        else:
            print(f"🐱{pet_name}: Sorry! Your food doesn't seem very common :)")

    print(f"\n 🍗🍟 The total calories of this meal will be {total_calories} 🍔🥤")
    return total_calories

def welcome_box():
    message = "🐱🐕🐘 Welcome to CaloPet 🐀🐖🐾"
    border = "      +" + "-" * (len(message) + 8) + "+"
    print(border)
    print(f"      | {message} |")
    print(border)
    print("\n🐱Ask your pet about food calories — stay fit & healthy!~~🐱")


def log_calories(time_period, calories, filename):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{time_period.capitalize()}: {calories} kcal\n")
