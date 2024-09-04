# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         CARTER LAIN
# Section:      544
# Assignment:   Lab 2.10
# Date:         8/29/2024


def interpolate_position(t, t1, t2, P1, P2):
    
    x1, y1, z1 = P1
    x2, y2, z2 = P2
    
    x = x1 + ((t - t1) / (t2 - t1)) * (x2 - x1)
    y = y1 + ((t - t1) / (t2 - t1)) * (y2 - y1)
    z = z1 + ((t - t1) / (t2 - t1)) * (z2 - z1)
    
    return (x, y, z)

def main():
    #data
    t1 = 12  # Start time 
    t2 = 85  # End time 
    P1 = (8, 6, 7)  # Position at t1
    P2 = (-5, 30, 9)  # Position at t2
    
    start_time = 30
    end_time = 60
    num_points = 5  # Number of points
    
    # Calculate evenly spaced time points
    time_points = [start_time + i * (end_time - start_time) / (num_points - 1) for i in range(num_points)]
    
    # Interpolate and print
    for i, t in enumerate(time_points):
        interpolated_position = interpolate_position(t, t1, t2, P1, P2)
        x, y, z = interpolated_position


        # Print the position
        print(f"At time {t:.1f} seconds:")
        print(f"x{i+1} = {x} m")
        print(f"y{i+1} = {y} m")
        print(f"z{i+1} = {z} m")

        #solution to get rid of last set of dashes
        if i < len(time_points) -1:
            ### solution above
            print("-" * 23)

if __name__ == "__main__":
    main()


## PROBLEM THAT IS LEFT = THE OUTPUT FOR X4 IS INCORRECT BY A FEW DECIMAL
##PLACES, FIGURE OUT WHAT HAPPENED


