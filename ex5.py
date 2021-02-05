my_name = 'Robin L Sharpton'
my_age = 50
my_height = 69
str_my_height_feet = "5"
str_my_height_inches = "9"
str_my_height_both = (f"{str_my_height_feet} foot {str_my_height_inches} inches")
my_weight = 180
my_eyes = 'gray'
my_teeth = 'white'
my_hair = 'blonde'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}")

print(f"My total height is {str_my_height_both}.")