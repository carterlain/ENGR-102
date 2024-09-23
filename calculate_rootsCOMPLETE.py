# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   Lab 4.21
# Date:         9/22/2024

import cmath

coeff_a = float(input('Please enter the coefficient A: ')) # A input
coeff_b = float(input('Please enter the coefficient B: ')) # B input
coeff_c = float(input('Please enter the coefficient C: ')) # C input

if coeff_a != 0:
    discriminant = coeff_b**2 - 4*coeff_a*coeff_c
    if discriminant >= 0:
        root_1 = (-coeff_b + discriminant**0.5) / (2*coeff_a)
        root_2 = (-coeff_b - discriminant**0.5) / (2*coeff_a)
    else:
        root_1 = (-coeff_b + cmath.sqrt(discriminant)) / (2*coeff_a)
        root_2 = (-coeff_b - cmath.sqrt(discriminant)) / (2*coeff_a)
elif coeff_a == coeff_b == 0:
    print('You entered an invalid combination of coefficients!')
elif coeff_a == 0:
    root_1 = -coeff_c / coeff_b
    root_2 = None

if root_2 is None:
    print(f'The root is x = {root_1}')
else:
    if root_1 == root_2:
        print(f'The root is x = {root_1}')
    elif isinstance(root_1, complex) or isinstance(root_2, complex):
        root_1_sign = '+' if root_1.imag >= 0 else '-'
        root_2_sign = '+' if root_2.imag >= 0 else '-'
        print(f'The roots are x = {root_1.real:.1f} {root_1_sign} {abs(root_1.imag):.1f}i and x = {root_2.real:.1f} {root_2_sign} {abs(root_2.imag):.1f}i')
    else:
        print(f'The roots are x = {root_1} and x = {root_2}')