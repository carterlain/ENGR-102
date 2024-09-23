# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   LAB 5.3
# Date:         9/22/2024

'''this was an absolute bitch fr'''

from math import *

# gather inputs
sex = str(input('Enter your sex (M/F): ')).strip().upper()
age = int(input('Enter your age (years): '))
bmi = float(input('Enter your BMI: '))
hypertension = str(input('Are you on medication for hypertension (Y/N)? ')).strip().upper()
steroid = str(input('Are you on steroids (Y/N)? ')).strip().upper()
smoker = input('Do you smoke cigarettes (Y/N)? ').strip().upper()
# special case for smokers, if do not currently smoke ask if used to smoke
if smoker == 'Y':
    used_smoker = 0
elif smoker == 'N':
    used_smoker = input('Did you used to smoke (Y/N)? ').strip().upper()
    smoker = 'N'
else:
    used_smoker = 'Invalid input'
# special case for family history, if family history ask if parent or sibiling or parent and sibling
family_hist = input('Do you have a family history of diabetes (Y/N)? ').strip().upper()
if family_hist == 'Y':
    parent_and_sib = input('Both parent and sibling (Y/N)? ').strip().upper()
else:
    parent_and_sib = 'N/A'

# derive values from inputs

# sex
if sex == 'F':
    sex = 0.879

if sex == 'M':
    sex = 0

# bmi    
if bmi < 25:
    bmi = 0

elif bmi <= 27.49:
    bmi = 0.699

elif bmi <= 29.99:
    bmi = 1.97

elif bmi >= 30:
    bmi = 2.518

# hypertension
if hypertension == 'N':
    hypertension = 0
else:
    hypertension = 1.222

# steriods
if steroid == 'N':
    steroid = 0
if steroid == 'Y':
    steroid = 2.191

# smokers
if used_smoker == 'Y':
    smoker_value = -0.218
elif used_smoker == 'N':
    smoker_value = 0
elif smoker == 'Y':
    smoker_value = 0.855
else:
    smoker_value = 'Invalid input'


#family history
if family_hist == 'N':
    family_hist_value = 0
elif parent_and_sib == 'Y':
    family_hist_value = 0.753
elif parent_and_sib == 'N':
    family_hist_value = 0.728
else:
    family_hist_value = 'Invalid input'

# calcuate risk
risk = 6.322 + sex - (0.063 * age) - bmi - hypertension - steroid - smoker_value - family_hist_value

#convert risk to percent
percent_risk = 100 / (1 + (e**risk))

#print risk
print(f'Your risk of developing type-2 diabetes is {percent_risk:.1f}%')