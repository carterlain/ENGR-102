# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      536
# Assignment:   Lab 4.18
# Date:         9/17/2024

num_1 = float(input('Enter number 1: '))
num_2 = float(input('Enter number 2: '))
num_3 = float(input('Enter number 3: '))

if num_1 > num_2 and num_1 > num_3: # print for when first number is largest
    print(f'The largest number is {num_1}')

if num_2 > num_1 and num_2 > num_3: # print for when second number is largest
    print(f'The largest number is {num_2}')

if num_3 > num_1 and num_3 > num_2: # print for when third number is largest
    print(f'The largest number is {num_3}')

if num_1 == num_2 or num_1 == num_3:
    print(f'The largest number is {num_1}')

if num_2 == num_3:
    print(f'The largest number is {num_2}')