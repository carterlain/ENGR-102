# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   Lab 4.15
# Date:         9/12/2024


from math import *

payed = float(input('How much did you pay? ')) # input for payed amount
cost = float(input('How much did it cost? ')) # input for cost 
change = 100 * (payed - cost) # multiply change by 100 to get in cents versus fractions of dollar

print(f'You received ${(change / 100):.2f} in change. That is...') # print how much change we have before calculating

'''determing # of coins'''

# Initialize variables
quarters = dimes = nickels = pennies = 0

if change >= 25: # if for calulating # of quarters
    quarters = change // 25 # divide change by value of quarter to get # of quarters
    change = round(change - (25 * quarters)) # subtract value of quarters from change to get new change value

if change >= 10: # if for calulating # of dimes
    dimes = change // 10 # divide change by value of quarter to get # of dimes
    change = round(change - (10 * dimes)) # subtract value of dimes from change to get new change value

if change >= 5: # if for calulating # of nickels
    nickels = change // 5 # divide change by value of quarter to get # of nickels
    change = round(change - (5 * nickels)) # subtract value of nickels from change to get new change value

if change >= 1: # if for calulating # of pennies
    pennies = change # set # of pennies equal to remaining change

    '''printing # of coins'''

if quarters == 0: # if # of quarters = 0, print nothing
    pass
elif quarters > 1: # if # of quarters is greater than 1, print multiple quarters
    print(f'{round(quarters)} quarters')
else: # if # of quarters = 1, print singular quarter
    print(f'{round(quarters)} quarter')

if dimes == 0: # if # of dimes = 0, print nothing
    pass
elif dimes > 1:# if # of dimes is greater than 1, print multiple dimes
    print(f'{round(dimes)} dimes')
else: # if # of dimes = 1, print singular dime
    print(f'{round(dimes)} dime')

if nickels == 0: # if # of nickels = 0, print nothing
    pass
elif nickels > 1: # if # of nickels is greater than 1, print multiple nickels
    print(f'{round(nickels)} nickels')
else: # if # of nickels = 1, print singular nickel
    print(f'{round(nickels)} nickel')

if change == 0: # if # of pennies/change = 0, print nothing
    pass
elif round(change) == 1: # if # of pennies = 1, print singular penny
    print(f'{round(change)} penny')
else: # if # of pennies is greater than 1, print multiple pennies
    print(f'{round(change)} pennies')