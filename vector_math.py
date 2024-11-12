# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   Lab 7.17
# Date:         11/7/2024

import math

vector_a = input('Enter the elements for vector A: ')
vector_b = input('Enter the elements for vector B: ')

# split both input vectors so they can be evaluated separately
split_a = vector_a.split(' ')
split_b = vector_b.split(' ')

# Ensure both vectors have the same length
if len(split_a) != len(split_b):
    print("Error: Vectors must be of the same length.")
else:
    # Convert string elements to floats
    split_a = [float(x) for x in split_a]
    split_b = [float(y) for y in split_b]

    # Magnitude of A
    magnitude_a = math.sqrt(sum(x**2 for x in split_a))

    # Magnitude of B
    magnitude_b = math.sqrt(sum(y**2 for y in split_b))

    # A + B
    AplusB = [split_a[i] + split_b[i] for i in range(len(split_a))]

    # A - B
    AminusB = [split_a[i] - split_b[i] for i in range(len(split_a))]

    # Dot product
    dot_product = sum(split_a[i] * split_b[i] for i in range(len(split_a)))

    print(f'The magnitude of vector A is {magnitude_a:.5f}')
    print(f'The magnitude of vector B is {magnitude_b:.5f}')
    print(f'A + B is {AplusB}')
    print(f'A - B is {AminusB}')
    print(f'The dot product is {dot_product:.2f}')