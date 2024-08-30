from math import *

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      536
# Assignment:   Lab 1.13
# Date:         8/22/2024

def evaluate_function(x):
    return (1-cos(x))/x**2

print('This shows the evaluation of (1-cos(x))/x^2 evaluated close to x=0') # print my explanation
print('my guess is 2')

for x in [1,0.1, 0.01,0.001,0.0001,0.00001,0.000001,0.0000001]:
    result = evaluate_function(x)
    print(f'{result}')

print('\n My guess was way off')
