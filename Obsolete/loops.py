






'''
+-----------------------------------+
| SIZE | LENGTH | Positions         |
|  0   |    0   |     []            |
|  1   |    0   |     []            |
|  0   |    1   |     []            |
|  1   |    1   | [[0][0]]          |
|      |        |                   |
|  2   |    2   |   [0, 0] [0, 0]   |
                    [1, 0] [0, 0]
                    [0, 0] [1, 0]
                    [1, 0] [1, 0]

                    [0, 1] [0, 0]
                    [1, 1] [0, 0]
                    [0, 1] [1, 0]
                    [1, 1] [1, 0]

                    [0, 0] [0, 1]
                    [1, 0] [0, 1]
                    [0, 0] [1, 1]
                    [1, 0] [1, 1]

                    [0, 1] [0, 1]
                    [1, 1] [0, 1]
                    [0, 1] [1, 1]
                    [1, 1] [1, 1]



'''


def recurse(positions, size, length):
    if size == 0 or length == 0:
        return
    if length != 5:
        return
    else:
        for pos in range(len(positions)):
            #xcords
            if pos == 0:
                max = size - 1
                for i in range(len(positions[pos])):
                    if positions[pos][i] < max:
                        
                        positions[pos][i] += 1
                        
                        print(positions)
                        recurse(positions,size,length )
            #ycods
            elif pos == 1:
                max = length - 1
                for i in range(len(positions[pos])):
                    if positions[pos][i] < max:
                        
                        positions[pos][i] += 1
                        
                        print(positions)
                        recurse(positions,size,length )
            else:
                print("FAIL")
                exit(1)
            
                
#        recurse(positions,size,length)
        
    


size = 3
length = 5

#xy cordinates for the starting postions of the Pentaminos
posx = [0 for i in range(size)]
posy = [0 for i in range(size)]

positions = [posx, posy]

#Gets all the posible starting positions for the board size
recurse(positions,size,length)


currIter = [0 for i in range(size)]
#
#for k in range(length):
#    for l in range(size):
#        for i in range(length):
#            for j in range(size):
#                print(f'{posx} {posy}')
#                posx[0] += 1
#
#            posx[0] = 0
#            posy[0] += 1
#        posy[0] = 0
#        print()
#
#        posx[1] += 1
#    posx[1] = 0
#    posy[1] += 1
#
    


