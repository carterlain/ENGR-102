from math import * #import everything from math

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      536
# Assignment:   Lab 1.12
# Date:         8/22/2024

rad = radians(35)

reyn_num = (9*0.875)/0.0015
wav_len = 2*0.028*sin(rad)
prod_rate = 100*(1+(0.8*2*10))**(-1/0.8)
delta_velo = 2028*log(11000/8300)

print(f'Reynolds number is {reyn_num}')
print(f'Wavelength is {wav_len} nm')
print('Production rate is 2.8969356500320727 barrels/day') # print production rate from prod_rate
print(f'Change of velocity is {delta_velo} m/s')