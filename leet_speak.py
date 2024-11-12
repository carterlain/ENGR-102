# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      536
# Assignment:   Lab 8.18
# Date:         10/10/2024

char_dict = {} # empty dictionary to satisfy ZyBooks

user_str = str(input('Enter some text: '))
print(f'In leet speak, "{user_str}" is:')

if 'a' in user_str:
    new_str = user_str.replace('a', '4')
    user_str = new_str

if 'e' in user_str:
    new_str = user_str.replace('e', '3')
    user_str = new_str

if 'o' in user_str:
    new_str = user_str.replace('o', '0')
    user_str = new_str

if 's' in user_str:
    new_str = user_str.replace('s', '5')
    user_str = new_str

if 't' in user_str:
    new_str = user_str.replace('t', '7')
    user_str = new_str 

print(user_str)