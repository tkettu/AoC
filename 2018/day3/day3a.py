import numpy as np

#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2

def claim(l):
    ids, _, coords, size = l.split(' ')
    x, y = map(int, coords[:-1].split(','))
    width, height = map(int, size.split('x'))
    return ids, x, y, width, height
                        
                    
fabric = np.zeros((1000, 1000))

#part 1
with open("input.txt") as f:

    for l in f:
        i, x, y, w, h = claim(l)
        fabric[x:x + w, y:y + h] += 1
    print( np.size(np.where(fabric >= 2)[0]))
    f.close()

#part 2
with open("input.txt") as f:

    for l in f:
        i, x, y, w, h = claim(l)
        if np.all(fabric[x:x + w, y:y + h] == 1):
            print(i)
    


    
    

        
