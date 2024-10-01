# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   Lab 6.19
# Date:         9/29/2024

from math import floor, sqrt

# gather inputs
integer = int(input('Enter a positive integer: '))

print(f'\nThe Juggler sequence starting at {integer} is:')

# while for jugglers sequence
iterations = 0
sequence = []
while integer > 1:
    sequence.append(integer)
    if integer % 2 == 0:
        integer = floor(sqrt(integer))
    else:
        integer = floor(integer**(3/2))
    iterations += 1

# append the last integer (which should be 1)
sequence.append(integer)

# print sequence
print(', '.join(map(str, sequence)))

# print # of iterations
print(f'It took {iterations} iterations to reach 1')
