# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Carter Lain
# Section:      544
# Assignment:   3.18
# Date:         5/9/2024

## user input stuff
quantity = float(input('Please enter the quantity to be converted: '))
""" Important note about mistake : make sure to distinguish between int and float for input types """

### Functions to convert the input to something
#pounds to newtons - N = P * 4.44822
newtons = quantity * 4.44822 
print(f'{quantity:.2f} pounds force is equivalent to {round(newtons, 2):.2f} newtons')

#meters to feet - Feet = Meters * 3.28084
meters = quantity * 3.28084
print(f'{quantity:.2f} meters is equivalent to {round(meters, 2):.2f} feet')

#atmospheres to kilopascals - KP = Atm. * 101.325
atmospheres = quantity * 101.325
print(f'{quantity:.2f} atmospheres is equivalent to {round(atmospheres, 2):.2f} kilopascals')


#watts to BTU - Watt = {BTU/hr}/{3.41...}
watts = quantity * 3.41214
print(f'{quantity:.2f} watts is equivalent to {round(watts, 2):.2f} BTU per hour')

#liters per second to gallons per minute - GPM = Liters/s * 15.8503
lps = quantity * 15.850323121489 ### needs to be percise asf
print(f'{quantity:.2f} liters per second is equivalent to {round(lps, 2):.2f} US gallons per minute')

#degrees celsius to degrees feranheit - F = (C * \frac{9}/{5}) + 32
celsius = quantity *(9/5) + 32
print(f'{quantity:.2f} degrees Celsius is equivalent to {round(celsius, 2):.2f} degrees Fahrenheit')