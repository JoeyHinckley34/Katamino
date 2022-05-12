
size = 2
length = 3

posx = [0 for i in range(size)]
posy = [0 for i in range(size)]

currIter = [0 for i in range(size)]


for k in range(length):
    for l in range(size):
        for i in range(length):
            for j in range(size):
                print(f'pos_x : {posx} \t pos_y : {posy}')
                posx[0] += 1
                        
            posx[0] = 0
            posy[0] += 1
        posy[0] = 0
        print()
    
        posx[1] += 1
    posx[1] = 0
    posy[1] += 1
    
    
