# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      536
# Assignment:   Lab 9.18
# Date:         11/7/2024

# function to get points
def getpoints(points_str):
    points = []
    pairs = points_str.split(' ')
    for pair in pairs:
        x, y = map(int, pair.split(','))
        points.append([x, y])
    return points

# function for cross product
def cross(point1, point2):
    return point1[0] * point2[1] - point1[1] * point2[0]

# function to get area
def shoelace(points):
    n = len(points)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += cross(points[i], points[j])
    return abs(area) / 2

# main to take print final
def main():
    points_str = input('Please enter the vertices: ')
    points = getpoints(points_str)
    area = shoelace(points)
    print(f'The area of the polygon is {area}')

if __name__ == '__main__':
    main()