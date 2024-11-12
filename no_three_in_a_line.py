# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Carter Lain
# Section:      544
# Assignment:   10.14
# Date:         10/24/2024

from itertools import combinations

def are_collinear(p1, p2, p3):
    """Check if three points are collinear using the determinant formula."""
    # (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1)
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) == (p2[1] - p1[1]) * (p3[0] - p1[0])


def no_three_in_line(n):
    """Find the largest set of points in an x n grid with no three in a line"""
    points = []
    
    # try to place points in the grid, avoiding three collinear points
    for i in range(n):
        for j in range(n):
            new_point = (i, j)
            valid = True

            # Check if the new point forms a collinear line with any two existing ponts
            for p1, p2 in combinations(points, 2):
                if are_collinear(p1, p2, new_point):
                    valid = False
                    break
            
       
            if valid:
                points.append((new_point))
    
    return points