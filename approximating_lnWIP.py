# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   Lab 6.15
# Date:         9/26/2024

from math import *

x = float(input('Enter a value for x: '))

while x <= 0 or x > 2:
    x = float(input('Out of range! Try again: '))
else:
    tol = float(input('Enter the tolerance: '))
    ln_approx = tol + 1
    n=1
    while ln_approx > tol:
        
        ln_approx = ((x-1)**n)/n
        n += 1
        k = n-1
    ln_exact = log(x)

def nat_log(X, a, K):
    total = 0
    for y in range(1,K+1):
        total += ((-1)**(y+1)*(X-a)**y)/y
        # print(((-1)**(y+1)*(X-a)**y)/y)
    return float(total)

print(f'ln({x}) is approximately {nat_log(x,1,n-2)}')
# print(f'ln({x}) is approximately {ln_approx}')
print(f'ln({x}) is exactly {ln_exact}')

difference = nat_log(x,1,n-2)-ln_exact

print(f'The difference is {difference}')