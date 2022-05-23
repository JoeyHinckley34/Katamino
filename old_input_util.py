import time

from matrix_util import rotate, transpose, Pentamino
from colors_util import bcolors, colorNums
from hashing_util import BinConvert, hashingVals

#@param filename : filename we are reading in 'Penatmino.txt'
#@returns allPentas: 3d array of all pentaminoes
def getPentas(filename):
    #opens file and reads it line by line
    with open(filename,'r') as myfile:
        data = myfile.read().splitlines()
    #Varibables
    allPentas = []
    penta = []
    #loop through all lines in .txt file
    for d in data:
        #if we get to a new shape add the shape to list and clear the current pentamino varible
        if d == '-':
            allPentas.append(penta)
            penta = []
        #otherwise add to the current pentaminoes shape
        else:
            penta.append([s for s in d])
    return allPentas
    
    
#@param allPC: List of Pentamino objects
#@returns allIters: The set of all possible orientations of all the Pentamino objects in allPC
def generateAllIters(allPC):
    allIters = set()
    for p in allPC:
        for i in range(4):
            p = rotate(p)
            allIters.add(p)
            
        p = transpose(p)
        allIters.add(p)

        for i in range(4):
            p = rotate(p)
            allIters.add(p)
    return allIters




def main():
    allPentas = getPentas('Pentamino.txt')

    #list of all pentamino objects
    allPC = []
    x = 0
    for i in allPentas:
        allPC.append(Pentamino(i,x))
        x += 1
        
#    for a in allPC:
#        print(a)
        
    #All possible iterations of all Pentaminoes
    allIters = generateAllIters(allPC)
    print("Set of all pentaminoes variations")
    for i in sorted(allIters):
        print(i)
        print(f'HASH VALUE: {i.gethash()}')

    

        
if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f'Executions time: {round(end - start,2)} seconds')
