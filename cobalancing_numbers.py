# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   Lab 6.20
# Date:         9/30/2024

# gather inputs and initialize variables
n = int(input('Enter a value for n: '))

less_sum = 0
great_sum = 0
r = 0

# Calculate the sum of numbers from 1 to n
for i in range(1, n+1):
    less_sum += i

# Reset i to start from n+1 and find the balancing point
i = n + 1
while great_sum < less_sum:
    great_sum += i
    i += 1
    r += 1

# print not a balancer if great_sum is more than less_sum
if great_sum > less_sum:
    print(f'{n} is not a co-balancing number')
# print is balancer if great_sum = less_sum
elif great_sum == less_sum:
    print(f'{n} is a co-balancing number with r={r}')