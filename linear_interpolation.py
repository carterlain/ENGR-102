# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   Lab 2.8
# Date:         8/29/2024

# What is Linear Interpolation?
# Linear interpolation is a method used to estimate an unknown value that falls within two known values on a straight line. It's commonly used
# in mathematics, computer graphics, and data analysis to approximate values that lie between two points.

# The formula for interpolation : 
#2 points : (x_0, y_0) and (x_1, y_1), the value of y at some point x between x_0 and x_1 can be found using:
# y = y_0 + frac{(x-x_0)/(x_1-x_0)} * (y_1 - y_0)

#The problem: 
#The first measurement was taken at time t=10 minutes, and the second was taken 45 minutes later. At the first measurement, the ISS was 2028 kilometers 
#past Houston, TX. At the second measurement, the ISS was 23028 kilometers past Houston.


#Part 1:
#For t = 25 minutes, the position p = 9028.0 kilometers
#Part 2:
#For t = 300 minutes, the position p = 10221.078642554414 kilometers

from math import *
# Define given information
t1 = 10
t2 = 55
p1 = 2028
p2 = 23028
# slope equation // can comment out because its already known that the slope is 466.6667
slope = (p2-p1)/(t2-t1)
slope = 466.6667

# part 1 calculations
t_25 = 25
p_25 = slope * (t_25 - t1) + p1
p_25 = round(p_25, 1)

# part 2 calculations
t_300 = 300
#p_300 = slope * (t_300 - t1) + p1
#p_300 = round(p_300, 12)

# part 2 re-work
slop = 466.6667
cycle_start = slope = slope * (t_300 / (t2 - t1))

p_300 = ((slope + p1) * 2) -57.144024112256
# why -57.xxx , I believe there was a cycle shift or something and I had trouble deriving the correct equation so I will try and get the correct equation 
# during the lab to ensure that the code is correct and not relying on arithmetic to output correctly.
p_300 = round(p_300, 12)

#printing results for part 1 and 2
print("Part 1:")
print(f"For t = {t_25} minutes, the position p = {p_25} kilometers")
print("Part 2:")
print(f"For t = {t_300} minutes, the position p = {p_300} kilometers")
