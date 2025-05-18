#The main program connects other codes
from Simple_calculation import calculate_total_calories, welcome_box, log_calories
from  FoodCalorie_data import food_calorie_table
from pet import Pet
from user_input import ask_pet_name, ask_new_pet_name, ask_meal_time, ask_first_food

import datetime




def main():
	
	welcome_box()
			
	today_str = datetime.date.today().isoformat()
	pet_name = ask_pet_name()
	filename = f"{pet_name.strip().lower()}.txt"
	log_filename = f"{pet_name.strip().lower()}_log_{today_str}.txt"

	try:
		pet = Pet.load_from_file(filename)
		print(f"\n       Welcome back! 🐱{pet_name}\n")
		print(pet)

	except FileNotFoundError:
		print("🐖: 'Oops~ I can't seem to find your pet. You can creat a new one...'") 
		pet_name = input("🐖: 'Give your pet a name:' ")
		pet = Pet(pet_name)
		pet.save_to_file(f"{pet_name.strip().lower()}.txt")
		print(f"\n🐱{pet_name}:  Hello World! ")


	time_period = ask_meal_time()

	first_food = ask_first_food(time_period)

	total_calories = calculate_total_calories(first_food,food_calorie_table, pet_name)
	
	pet.eat(first_food, total_calories)

	log_calories(time_period, total_calories, log_filename)
	
	pet.save_to_file(filename)
	print(pet)
	print("Success! Calories recorded and pet updated.")
	
	





if __name__ == "__main__":
    main()
