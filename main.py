#Standard Imports
import numpy as np
import binary
import time
#Custom Imports
import testing
from input_util import getAllPents
from helper_functions import dec_to_bin_zeros
from solver import board

def main():
    DEBUG = 1

    allPents = getAllPents(DEBUG)
    
    if(DEBUG):
        numFixed = 0
        for p in allPents:
            numFixed += len(p.pentas)
            print(p)
        print(f'Number of fixed pentaminoes: {numFixed} \nNumber of free pentaminoes:  {len(allPents)}')
    
    #################################################
    #################################################
    BOARD_SIZE = 3 #<--- Change to maximum board size
    #################################################
    #################################################
    
    #Loop through all Pents calculate all their positions on the board
    counter = 0
    for p in range(len(allPents)):
        for q in range(len(allPents[p].pentas)):
            counter += 1
            
            allPents[p].pentas[q].mult = binary.multiplyList(allPents[p].pentas[q].shapeN,BOARD_SIZE)
            for m in allPents[p].pentas[q].mult:
                allPents[p].pentas[q].allPos.append(binary.addzeros(m,5))
            
            allPents[p].Full.append((allPents[p].pentas[q].allPos))

            # if(DEBUG):
            #     print(allPents[p].pentas[q])
            #     print(f'{counter}: \t{allPents[p].pentas[q].mult} \n\t{allPents[p].pentas[q].allPos} ')

    # if (DEBUG):
    #     #Print the 12 pentaminos in every position on the board
    #     for p in range(len(allPents)):
    #         print(f'\n{allPents[p].Full}')

    for p in range(len(allPents)):
        for f in range(len(allPents[p].Full)):
            for a in range(len(allPents[p].Full[f])):
                for b in range(len(allPents[p].Full[f][a])):
#                    print(allPents[p].Full[f][a][b])
                    cur_row = []
                    for c in range(len(allPents[p].Full[f][a][b])):
                        
                        bin_row =  str(dec_to_bin_zeros( allPents[p].Full[f][a][b][c],BOARD_SIZE))
                        for d in bin_row:
                            cur_row.append(int(d))
                    
                    #Only add shapes that fit in the board
                    #When the board is larger than 5 all shapes fit
                    if (BOARD_SIZE > 5):
                        allPents[p].BinFull.append(cur_row[:])
                    elif (len(cur_row ) == (BOARD_SIZE*5)):
                        allPents[p].BinFull.append(cur_row[:])
                                                
    # if(DEBUG):
    #     for p in range(len(allPents)):
    #         print(allPents[p])
    #         for r in range(len( allPents[p].BinFull)):
    #             print(allPents[p].BinFull[r])
    #         print()
    
    
################
#Bin Solver Test#
################

#    testing.testBinOne(allPents[4])
#    testing.testBinThree(allPents,[4,5,11])

#    testing.testBinAll(allPents,BOARD_SIZE,[4,5,11],0)
    #testing.testBinAll(allPents,BOARD_SIZE,[4,5,11,1],0)

#    testing.testBinAll(allPents,BOARD_SIZE,[4,5,11,1,3],0)
#    testing.testBinAll(allPents,BOARD_SIZE,[4,5,11,1,3,9],0)
    
#    testing.testBinIters(allPents,BOARD_SIZE)

####################
#Dancing Links Tests#
####################

#    testing.testAll3iter(allPents)
#    testing.testAll3(allPents)

    testing.testAll(allPents,BOARD_SIZE)

#    testing.testAllDups(allPents,BOARD_SIZE)
    
#    testing.testAll4x2(allPents)
#    testing.testAll5x2(allPents)
#    testing.testAll6x2(allPents)
     
#    testing.SMALL_SLAM_A(allPents)
#    testing.tilingPlane(allPents,BOARD_SIZE)

if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f'Executions time: {round(end - start,2)} seconds')
