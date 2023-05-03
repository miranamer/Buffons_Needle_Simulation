import random as rd
import numpy as np

def generate_needles(bounds, lines, l):

    needles = []
    
    for _ in range(lines):
        x1, y1, x2 = rd.sample(range(bounds), 3)
        
        a = x2 - x1

        while a >= l or a <= 0: # a cant be bigger than l as its a right angle triangle and pythagoras wont work otherwise
            x1, y1, x2 = rd.sample(range(bounds), 3)
            a = x2 - x1
        
        squared_diff = (l**2 - a**2) # = b^2

        #print(l**2, a**2, l, a, squared_diff)
        
        b = np.sqrt(squared_diff)

        y2 = b + y1

        line_distance = np.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

        needles.append((x1, y1))
        needles.append((x2, y2))

        #print(f'p1:{x1, y1} ~ p2:{x2, y2} |line| => {line_distance}')
    
    return needles

#print(generate_needles(20, 1, 4))

        