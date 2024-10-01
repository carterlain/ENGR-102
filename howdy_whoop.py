# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   Lab 6.16
# Date:         9/29/2024

int_1 = int(input('Enter an integer: '))
int_2 = int(input('Enter another integer: '))
print('\n')

for i in range(1, 101):  # range set from 1 to 100 stepping by 1

    if i % int_1 != 0 and i % int_2 != 0:
        print(i)

    if i % int_1 == 0 and i % int_2 != 0:
        print('Howdy')

    if i % int_1 != 0 and i % int_2 == 0:
        print('Whoop')

    if i % int_1 == 0 and i % int_2 == 0:
        print('Howdy Whoop')
