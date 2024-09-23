# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   LAB 4.14
# Date:         9/19/2024

from math import *

# gather inputs
hypotenuse = float(input('Enter the hypotenuse: '))
opp_side = float(input('Enter the opposite side: '))
adj_side = float(input('Enter the adjacent side: '))

# determine if the inputs create a right trianlge
# if they do, ask which trig function to use
if hypotenuse > opp_side and hypotenuse > adj_side:
    trig_func = int(input("What would you like to calculate?\n1: sin(θ), 2: cos(θ), 3: tan(θ), 4: csc(θ), 5: sec(θ), 6: cot(θ): "))
# if they don't, print error
else:
    print("Those lengths don't form a right triangle!")

# sin function
if trig_func == 1:
    theta = opp_side/hypotenuse
    print(f'For a right triangle of sides {opp_side}, {adj_side}, and {hypotenuse}, sin(θ) = {theta:.1f}')

#cos function
elif trig_func == 2:
   theta = adj_side/hypotenuse
   print(f'For a right triangle of sides {opp_side}, {adj_side}, and {hypotenuse}, cos(θ) = {theta:.1f}')

#tangent function
elif trig_func == 3:
   theta = opp_side/adj_side
   print(f'For a right triangle of sides {opp_side}, {adj_side}, and {hypotenuse}, tan(θ) = {theta:.1f}')

#cosecant function
elif trig_func == 4:
   theta = hypotenuse/opp_side
   print(f'For a right triangle of sides {opp_side}, {adj_side}, and {hypotenuse}, csc(θ) = {theta:.1f}')

# secant function
elif trig_func == 5:
   theta = hypotenuse/adj_side
   print(f'For a right triangle of sides {opp_side}, {adj_side}, and {hypotenuse}, sec(θ) = {theta:.1f}')

# cotangent function
elif trig_func == 6:
   theta = adj_side/opp_side
   print(f'For a right triangle of sides {opp_side}, {adj_side}, and {hypotenuse}, cot(θ) = {theta:.1f}')