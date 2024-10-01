# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   Lab 6.11
# Date:         9/26/2024

# gather inputs
side_len = float(input('Enter the side length in meters: '))
layer = int(input('Enter the number of layers: '))

# initialize variables
surface_area = 0
i = layer

for layer in range(layer,0,-1):
    temp_surface_area = (layer**2) + (layer * 4) - (layer-1)**2
    surface_area += side_len**2 * temp_surface_area
   
print(f'You need {surface_area:.2f} m^2 of gold foil to cover the pyramid')