from utils import input_until_right


fist_name = input_until_right("First name: ", "invalid type for a first name, please try again")
second_name = input_until_right("Second name: ", "invalid type for a second name, please try again")

print(f"Your full name is {fist_name} {second_name}")