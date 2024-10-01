# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   Lab 6.12
# Date:         9/26/2024

side_len = float(input('Enter the side length in meters: '))
layer = int(input('Enter the number of layers: '))

# calculate the total surface area using arithmetic progression
n = layer
sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
sum_of_linear_terms = n * (n + 1) // 2
sum_of_previous_squares = (n - 1) * n * (2 * (n - 1) + 1) // 6

surface_area = side_len**2 * (sum_of_squares + 4 * sum_of_linear_terms - sum_of_previous_squares)

print(f'You need {surface_area:.2f} m^2 of gold foil to cover the pyramid')
