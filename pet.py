#The home of pets
import datetime
today_str = datetime.date.today().isoformat()

pets = ('🐱',)

class Pet:
	def __init__(self, name):
		self.name = name
		self.calories = 0
		self.weight = 5
		self.mood = "happy :)"
		


	def eat(self, food , calorie):
		self.calories += calorie

		#total_calories = self.calories

		if self.calories > 2000:
			self.mood = "too full😵"
			print("Today, we ate too much !!!")
			
		elif self.calories < 2000 and self.calories > 1000:
			self.mood = "So delicious! Happy!"

		elif self.calories < 1000:
			self.mood = "Great! I'm going to lose weight !"
			print("Still a bit hungry.")

		self.update_weight()

	def update_weight(self):

		self.weight += (self.calories - 1000)/10000

	

	def __str__(self) -> str:
	        # Returns a status of the pet after meal
	        return (f"Status Report - 🐱{self.name} - {today_str}\n"
	                + "-" * 35 + "\n"
	                + f"Calorie intake     : ({self.calories})\n"
	                + f"Weight             : {self.weight:.2f} Kg\n"
	                + f"Mood               : {self.mood}\n"
	                + "-" * 35)


	def save_to_file(self, filename):
	    with open(filename, "w", encoding="utf-8") as file:
	        file.write(f"{self.name}\n")
	        file.write(f"{self.calories}\n")
	        file.write(f"{self.weight}\n")
	        file.write(f"{self.mood}\n")



	@staticmethod
	def load_from_file(filename):
		with open(filename, "r", encoding="utf-8") as file:
		    name = file.readline().strip()
		    calories = int(file.readline().strip())
		    weight = float(file.readline().strip())
		    mood = file.readline().strip()

		    pet = Pet(name)
		    pet.calories = calories
		    pet.weight = weight
		    pet.mood = mood
		    return pet

