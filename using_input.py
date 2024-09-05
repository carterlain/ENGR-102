from math import * #import everything from math

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        
# Section:      544
# Assignment:   3.18
# Date:         5/9/2024
#

# Reynolds # function
print('This program calculates the Reynolds number given velocity, length, and viscosity')
velocity = float(input('Please enter the velocity (m/s): ')) # input for velocity as float
length = float(input('Please enter the length (m): ')) # input for length as float
viscosity = float(input('Please enter the viscosity (m^2/s): ')) # input for viscosity as float

reyn_num = int((velocity*length)/viscosity) # Reynolds # equation
reyn_num = round(reyn_num, -1)

print(f'Reynolds number is {reyn_num}') # print result of equation

print('\n')

# Wavelength function
print('This program calculates the wavelength given distance and angle')
distance = float(input('Please enter the distance (nm): ')) # input for distance as float
angle = float(input('Please enter the angle (degrees): ')) # input for angle as float
rad = radians(angle) # converts angle input to radians

wav_len = 2*distance*sin(rad) # wavelength equation

print(f'Wavelength is {wav_len:.4f} nm') # print result of equation

print('\n')

# Barrel production rate function
print('This program calculates the production rate given time, initial rate, and decline rate')
time = float(input('Please enter the time (days): ')) # input for time as float
initial_rate = float(input('Please enter the initial rate (barrels/day): ')) # input for initial rate as float
decline_rate = float(input('Please enter the decline rate (1/day): ')) # input for decline rate as float

prod_rate = initial_rate*(1+(0.8*decline_rate*time))**(-1/0.8) # production rate equation

print(f'Production rate is {prod_rate:.2f} barrels/day') # print results of equation

print('\n')

# Change in velocity function
print('This program calculates the change of velocity given initial mass, final mass, and exhaust velocity')
initial_mass = float(input('Please enter the initial mass (kg): ')) # input for initial mass as float
final_mass = float(input('Please enter the final mass (kg): ')) # input for final mass as float
exhaust_velo = float(input('Please enter the exhaust velocity (m/s): ')) # input for exhaust velocity as float


delta_velo = exhaust_velo*log(initial_mass/final_mass) # change in velocity equation

print(f'Change of velocity is {delta_velo:.1f} m/s') # print results of equation