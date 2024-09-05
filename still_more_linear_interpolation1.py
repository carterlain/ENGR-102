t1 = float(input('Enter time 1: '))
x1 = float(input('Enter the x position of the object at time 1: '))
y1 = float(input('Enter the y position of the object at time 1: '))
z1 = float(input('Enter the z position of the object at time 1: '))

t2 = float(input('Enter time 2: '))
x2 = float(input('Enter the x position of the object at time 1: '))
y2 = float(input('Enter the y position of the object at time 1: '))
z2 = float(input('Enter the z position of the object at time 1: '))

while 1 == 1:
    if t1<t2:  
        print (f'At time {t1:.2f} seconds the object is at ({x1:.3f}, {y1:.3f}, {z1:.3f})')
    t1 += 0.25
    x1 += 0.25
    y1 += 0.25
    z1 += 0.25
else:
    quit()