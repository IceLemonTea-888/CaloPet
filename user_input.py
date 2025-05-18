#This is where the system collects the documents input by the users.

def ask_pet_name():
    return input("\nEnter your pet's name to load: ").strip().lower()
    
def ask_new_pet_name():
    return input(" \nGive your pet a name!!!")
    
def ask_meal_time():
    return input(f"\n Are you going to have breakfast, lunch or dinner now? ").strip().lower()
    
def ask_first_food(time_period):
    return input(f"\n What are you going to have for {time_period}? ").strip().lower()
