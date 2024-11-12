# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      536
# Assignment:   Lab 6.21
# Date:         11/5/2024

def is_balancing_number(n):
    # Calculate the sum from 1 to (n-1)
    sum_left = 0
    for i in range(1, n):
        sum_left += i

    # Initialize sum for the right side and the value of r
    r = 1
    sum_right = 0

    # Calculate the sum from (n+1) to (n+r) iteratively
    while True:
        sum_right += (n + r)
        # Check if sums are equal
        if sum_right == sum_left:
            return r
        # If the sum_right exceeds sum_left, it's not a balancing number
        if sum_right > sum_left:
            return None
        r += 1

if __name__ == "__main__":
    n = int(input("Enter a value for n: "))
    result = is_balancing_number(n)
    if result:
        print(f"{n} is a balancing number with r = {result}")
    else:
        print(f"{n} is not a balancing number")
