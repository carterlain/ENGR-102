# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   LAB 5.5
# Date:         9/24/2024

from math import *

excess_temp = float(input('Enter the excess temperature: '))

# linear approximations of different boiling curve regions
free_convection_m = (log10(7000/1000))/(log10(5/1.3))
free_convection = 1000 * (excess_temp/1.3)**free_convection_m

nucleate_boiling_m = (log10(1.5e6/7000))/(log10(30/5))
nucleate_boiling = 7000 * (excess_temp/5)**nucleate_boiling_m

transition_region_m = (log10(2.5e4/1.5e6))/(log10(120/30))
transition_region = 1.5e6 * (excess_temp/30)**transition_region_m

film_region_m = (log10(1.5e6/2.5e4))/(log10(1200/120))
film_region = 2.5e4 * (excess_temp/120)**film_region_m

# use if temperature is less than minimum start temperature (1.3)
if excess_temp <= 1.3:
    print(f'Surface heat flux is not available')

# use if temperature is in free convection area
elif excess_temp > 1.3 and excess_temp <= 5:
    print(f'The surface heat flux is approximately {free_convection:.0f} W/m^2')

# use if temperature is in nucleate area
elif excess_temp <= 30:
    print(f'The surface heat flux is approximately {nucleate_boiling:.0f} W/m^2')

# use if temperature is in transition area
elif excess_temp <= 120:
    print(f'The surface heat flux is approximately {transition_region:.0f} W/m^2')

# use if temperature is in film area
elif excess_temp < 1200:
    print(f'The surface heat flux is approximately {film_region:.0f} W/m^2')

# use if temperature is not on graph (<0)
else:
    print(f'Surface heat flux is not available')