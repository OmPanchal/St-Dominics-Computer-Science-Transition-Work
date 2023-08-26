WEIGHTS_TO_POUNDS =  2.20462
POUNDS_TO_STONE = 14

Weight_KG = float(input("What is your weight in KG?: "))


Pounds = Weight_KG * WEIGHTS_TO_POUNDS
Stones = Pounds // POUNDS_TO_STONE

Remainder_Pounds = Pounds - (Stones * POUNDS_TO_STONE)

print("STONES:", Stones, "POUNDS:", Remainder_Pounds)