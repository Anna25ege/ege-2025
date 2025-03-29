for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (not w <= (x == y or y)) and (z <= x)
                if f == 1:
                    print(x,w,z,y)