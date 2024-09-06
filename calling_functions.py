# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   Lab 3.20
# Date:         9/5/2024

from math import * # import all math
# printresult creates blanket print that can manipulated later when called

def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

side_len = float(input('Please enter the side length: ')) # input for side length as float

triangle_area = ((sqrt(3))/4)*(side_len**2) # equilateral triangle area
square_area = side_len**2 # square area
pentagon_area = (1/4)*(sqrt(5*(5+2*(sqrt(5)))))*(side_len**2) # pentagon area
hexagon_area = ((3*(sqrt(3)))/2)*(side_len**2) # hexagon area
dodecagon_area = 3*(2+(sqrt(3)))*(side_len**2) # dodecagon area

printresult('triangle', side_len, triangle_area) # inserting values for trianlge
printresult('square', side_len, square_area) # for square
printresult('pentagon', side_len, pentagon_area) # for pentagon
printresult('hexagon', side_len, hexagon_area) # for hexagon
printresult('dodecagon', side_len, dodecagon_area) # for dodecagon