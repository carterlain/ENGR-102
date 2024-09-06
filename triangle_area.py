# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   Lab 3.15
# Date:         9/5/2024

from math import * # import all math

# Input values
x = float(input('Enter the value of x: '))  # Large square side length
y = float(input('Enter the value of y: '))  # Small square side length

# Coordinates of the triangle vertices
A = (0, x)         # Top left corner of the bigger square
B = (x + y, 0)     # Bottom right corner of the smaller square
C = (x, y)         # Top left corner of the smaller square

# Calculate the lengths of the sides of the triangle
AB = sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)
BC = sqrt((C[0] - B[0])**2 + (C[1] - B[1])**2)
CA = sqrt((A[0] - C[0])**2 + (A[1] - C[1])**2)

# Calculate the semi-perimeter
s = (AB + BC + CA) / 2

# Calculate the area using Heron's formula
area = sqrt(s * (s - AB) * (s - BC) * (s - CA))

# Print the area of the triangle
print(f'The area of the triangle is {area:.3f}')
