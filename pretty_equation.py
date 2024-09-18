# By submitting this assignment, I agree to the following:
#   'Aggies do not lie, cheat, or steal, or tolerate those who do.'
#   'I have not given or received any unauthorized aid on this assignment.'
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   Lab 4.16
# Date:         9/17/2024

A = int(input('Please enter the coefficient A: '))
B = int(input('Please enter the coefficient B: '))
C = int(input('Please enter the coefficient C: '))

def coefficient_a():
    if A == 0:
        return ''
    
    elif A == 1:
        return 'x^2'
    
    elif A == -1:
        return '- x^2'
    
    elif A < 0:
        return f'- {abs(A)}x^2'
    
    else:
        return f'{A}x^2'

def coefficient_b():
    if B == 0:
        return ''
    
    elif B == 1:
        return '+ x'
    
    elif B == -1:
        return '- x'
    
    elif B < 0:
        return f'- {abs(B)}x'
    
    else:
        return f'+ {B}x'

def coefficient_c():
    if C == 0:
        return ''
    
    elif C < 0:
        return f'- {abs(C)}'
    
    else:
        return f'+ {C}'

# Construct the polynomial
polynomial = f'{coefficient_a()} {coefficient_b()} {coefficient_c()}'.strip()

# Clean up the polynomial string
polynomial = ' '.join(polynomial.split())

if polynomial.startswith('+ '):
    polynomial = polynomial[2:]

print(f'The quadratic equation is {polynomial} = 0')