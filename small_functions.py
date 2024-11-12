# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   Lab 9.20
# Date:         10/25/2024

from math import *

def parta (r_sphere, r_hole):
    volume = ((4*pi)/3)*(r_sphere**2 - r_hole**2)**(3/2) # condensed formula for volume of sphere with hole in middle
    
    return volume


def partb (n):
    for start in range(2, n, 2):  # Start with the first even number and iterate
        total = 0
        consecutive = []
        for even in range(start, n, 2):  # Generate consecutive even numbers
            total += even
            consecutive.append(even)
            if total == n:  # If the sum matches n, return the list
                return consecutive
            elif total > n:  # If the sum exceeds n, move to the next starting even number
                break
    
    return False  # If no match found, return False


def partc(border_char, name, company, email):
    entries = [name, company, email]
    max_length = max(len(entry) for entry in entries)
    card_width = max_length + 6  # Adding 2 spaces on each side and the border characters
    border_line = border_char * card_width
    
    formatted_entries = [f"{border_char}  {entry.center(max_length)}  {border_char}" for entry in entries]
    
    card = [border_line] + formatted_entries + [border_line]
   
    return "\n".join(card)


def partd(input_list):
    input_list.sort()
    min_num = input_list[0]
    max_num = input_list[-1]
    
    if len(input_list) % 2 != 0: # evaluates wether list is odd or even length
        median_num = input_list[len(input_list) // 2]
    else:
        mid_index = len(input_list) // 2
        median_num = (input_list[mid_index - 1] + input_list[mid_index]) // 2
    
    return min_num, median_num, max_num


def parte (times, distances):
    velocities = []
    for i in range(1, len(times)): # iterate from 1 to 1-number of times passed in
        delta_time = times[i] - times[i - 1]
        delta_distance = distances[i] - distances[i - 1]
        velocity = delta_distance / delta_time
        velocities.append(velocity)
    
    return velocities


def partf(numbers):
    num_set = set()
    for number in numbers: # iterates through numbers in list
        target = 2028 - number
        if target in num_set:
            return target * number
        num_set.add(number)
    return False