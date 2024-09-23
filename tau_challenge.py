# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   LAB 3.21
# Date:         9/22/2024

from math import *

# gather inputs
tau_digits = int(input('Please enter the number of digits of precision for tau: '))

# use decimal rounding in f string as variable instead of fixed number
print(f'The value of tau to {tau_digits} digits is: {tau:.{tau_digits}f}') 