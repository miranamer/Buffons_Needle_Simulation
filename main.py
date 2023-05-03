import numpy as np
import matplotlib.pyplot as plt
import needle_generation
import validate_crossings

t = 4
pieces = 5
l = t//2

bounds = []

needles = needle_generation.generate_needles(t*pieces, 20, t) # change l (in this case set to t) to change needle length

x = [i[0] for i in needles]
y = [i[1] for i in needles]

line_x_coords = []

for i in range(0, len(x), 2):
    line_x_coords.append([x[i], x[i+1]])

#print(f'line_x_coords ->', line_x_coords)


ranges = []

for i in range((pieces*t) + 1):
    if i % t == 0:
        bounds.append(i)

ptr = 0
while ptr < len(bounds) - 1:
    ranges.append((bounds[ptr], bounds[ptr+1]))
    ptr += 1

#print('t:', t, 'pieces:', pieces, 'bounds:', bounds, 'ranges:', ranges)

all_crossings = validate_crossings.validate_crossings(line_x_coords, ranges)

for i in range(0, len(x), 2):
    if x[i:i+2] in all_crossings:
        plt.plot(x[i:i+2], y[i:i+2], 'r')
    else:
        plt.plot(x[i:i+2], y[i:i+2], 'c')


for x in bounds:
    plt.axvline(x=x)

plt.show()