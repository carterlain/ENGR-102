# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   Lab 4.21
# Date:         9/16/2024

coeff_a = float(input('Please enter the coefficient A: ')) # A input
coeff_b = float(input('Please enter the coefficient B: ')) # B input
coeff_c = float(input('Please enter the coefficient C: ')) # C input

root_2 = 0

if coeff_a != 0:
    root_1 = (-coeff_b + ((coeff_b**2)-4*coeff_a*coeff_c)**(1/2))/(2*coeff_a)
    root_2 = (-coeff_b - ((coeff_b**2)-4*coeff_a*coeff_c)**(1/2))/(2*coeff_a)
elif coeff_a == coeff_b == 0:
    print ('You entered an invalid combination of coefficients!')

elif coeff_a == 0:
    root_1 = -coeff_c/coeff_b

if root_1 == 0 or root_2 ==0 or root_1 == root_2:
    print(f'The root is x = {root_1}')
else:
    print(f'The roots are x = {root_1} and x = {root_2}')