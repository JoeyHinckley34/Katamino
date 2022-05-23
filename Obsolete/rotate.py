"""
Katamino rotate
"""

import numpy as np

brn = np.array([[1,0],[1,1],[1,0],[1,0]])
orng = np.array([[1,1],[1,0],[1,0],[1,0]])

def rotate (pentamino):
    """function to rotate a shape 90 deg CW"""
    lengthy = np.size(pentamino,0)      
    lengthx = np.size(pentamino,1)      
    newshape = np.zeros((lengthx,lengthy))

    for x in range(0,lengthx):
        for y in range(0,lengthy):
            newshape[x,y] = pentamino[lengthy-y-1,x]     
    return newshape
    
print(np.transpose(rotate(rotate(brn))))
