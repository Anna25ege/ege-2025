for x in range(2):
    for y in  range(2):
        for w in range(2):
            for z in range(2):
                f = x and (z <= y == w)
                if f == 1:
                    print(w,y,x,z)