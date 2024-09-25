# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   Lab 3.16
# Date:         9/23/2024

from math import *

############ Part 1 ############
print('Part 1')

# gather inputs
height = float(input('Enter the height of the door: '))
width = float(input('Enter the width of the door: '))

area = height * width + (width**2) * ((2 - 4 * sqrt(2) + pi)/ 8)

print(f'The area of the door is {area:.2f}')
# calculate area


############ Part 2 ############
print('\nPart 2')

# gather inputs
height = float(input('Enter the height of the pyramid: '))

x = height * (sqrt(2))
surf_area = (x**2) * (sqrt(3)) + (x**2)

print(f'The surface area of the pyramid is {surf_area:.2f}')

############ Part 3 ############
print('\nPart 3')

# gather inputs
area = float(input('Enter the area of a triangle: '))

side_a = (2/3)*(3**(3/4))*(sqrt(area))
side_b = sqrt(2 * side_a**2 + 2 * sqrt(side_a**4 - 4 * area**2))
side_c = (2 * area)/ side_b
side_d = sqrt((side_b**2) + (side_c**2))
sin_e = (2 * area) / (side_a * side_d)
cos_e = sqrt(1 - sin_e**2)
side_e = sqrt(side_a**2 + side_d**2 - 2 * side_a * side_d * cos_e)

print(f'The equilateral triangle has sides with length {side_a:.2f}')
print(f'The isosceles triangle has two sides with lengths {side_a:.2f} and one side with length {side_b:.2f}')
print(f'The right triangle has sides with lengths {side_b:.2f}, {side_c:.2f}, and {side_d:.2f}')
print(f'The arbitrary triangle has sides with lengths {side_a:.2f}, {side_d:.2f}, and {side_e:.2f}')