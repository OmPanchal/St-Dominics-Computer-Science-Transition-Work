from utils import input_until_right

num1 = input_until_right("First Number: ", "invalid input type, please try again...", float)
num2 = input_until_right("Second Number: ", "invalid input type, please try again...", float)

total = num1 + num2

print(f"{num1} + {num2} = {total}")