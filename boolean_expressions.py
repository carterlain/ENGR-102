# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   LAB 4.17
# Date:         9/19/2024

############ Part A ############

a = input("Enter True or False for a: ").lower() in ["true", "t"]
b = input("Enter True or False for b: ").lower() in ["true", "t"]
c = input("Enter True or False for c: ").lower() in ["true", "t"]

print(f"a and b and c: {a and b and c}") # checks if a,b,c are the same
print(f"a or b or c: {a or b or c}") # checks if any are true
print(f"XOR: {((not a) and b) or (a and (not b))}") # checks if one is true and one is false

############ Part B ############

print(f"Odd number: {((a and not b and not c) or (not a and b and not c) or (not a and not b and c) or (a and b and c))}") # checks if True was entered 1 or 3 times

############ Part C ############

expression1 = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
expression2 = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))

print(f"Expression 1: {expression1}")
print(f"Expression 2: {expression2}")