# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   Lab 6.17
# Date:         9/29/2024

# gather inputs
int_1 = int(input('Enter an integer: '))
int_2 = int(input('Enter another integer: '))

# calculate intergers between inputs and find sum
i = int_1
sum_ints = 0
while i < int_2 + 1:
    sum_ints += i
    i += 1

# print sum
print(f'The sum of all integers from {int_1} to {int_2} is {sum_ints}')