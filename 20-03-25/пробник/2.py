for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((w and y) or (x <= w == y <= z))
                if f == 0:
                    print(z,w,y,x)