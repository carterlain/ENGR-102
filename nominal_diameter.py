# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   LAB 4.13
# Date:         9/19/2024

#gather inputs
nominal_dia = float(input('Enter the nominal diameter: '))
actual_dia = float(input('Enter the actual diameter: '))

# calculate percent difference between nominal and actual
percent_diff = abs((actual_dia - nominal_dia) / nominal_dia) * 100

# if difference is less than 1% print this
if percent_diff < 1:
    print('The diameter is within <1% of desired value')

# less than 2% print this
elif percent_diff <= 2:
    print('The diameter is between 1% and <2% of desired value')

# less than 5% print this
elif percent_diff <= 5:
    print('The diameter is between 2% and <5% of desired value')

# greater than 5% print this
elif percent_diff > 5:
    print('Out of specifications, >=5% error')