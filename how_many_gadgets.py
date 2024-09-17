# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   Lab 4.20
# Date:         9/16/2024

days = int(input('Please enter a positive value for day: '))

if days < 0:
    print('You entered an invalid number!')
    pass

elif days <= 10: # gadgets produced on days 0 to 10
    gadgets = 0
    gadgets = 10*days
    print(f'The sum total number of gadgets produced on day {days} is {gadgets}')

elif days >= 11 and days <= 50: # gadgets produced on days 11 to 50
    num_days = days - 11 + 1
    gadgets = int(100 + ((num_days/2) * (11+(10 + num_days)))) # eqaution which increases prodcution by one for every day e.g. 11 days = 11 gadgets
    print(f'The sum total number of gadgets produced on day {days} is {gadgets}')

elif days >= 51 and days <= 100: # gadgets produced on days 51 to 100
    gadgets = int(1320 + ((days - 50)*50))
    print(f'The sum total number of gadgets produced on day {days} is {gadgets}')

elif days > 100: # gadgets produced after day 100
    gadgets = 3820
    print(f'The sum total number of gadgets produced on day {days} is {gadgets}')