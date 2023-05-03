def validate_crossings(line_x_coords, ranges):
    range_vals = []

    crossings = []

    for i in ranges:
        vals = [x for x in range(i[0], i[1]+1)]
        range_vals.append(vals)
    
    for x1, x2 in line_x_coords:
        overlaps = []
        for i in range_vals:
            if x1 in i:
                overlaps.append(i[0]+i[-1])
            if x2 in i:
                overlaps.append(i[0]+i[-1])
    
        #print(overlaps)

        if len(list(set(overlaps))) != len(overlaps):
            None
        else:
            #print(f'Crossing! - {x1, x2}')
            crossings.append([x1, x2])
    
    return crossings


#print(validate_crossings([[7, 9], [3, 5]], [(0, 4), (4, 8), (8, 12), (12, 16), (16, 20)]))