#Standard Imports
import numpy as np
import binary
import itertools
import time
#Custom Imports
from colors_util import bcolors, colorNums
from hashing_util import BinConvert, hashingVals
import Kunths
import testing

#HELPER FUNCTIONS
#@param x : Number in base ten
#@returns : x in binary
def dec_to_bin(x):
    return int(bin(x)[2:])

#@param x : Number to be converted to binary
#@param z : Number of leading zeros
#@returns : x in binary with z leaing zeros
def dec_to_bin_zeros(x,z):
    return f'{int(bin(x)[2:]):0{z}}'

class Pentamino:
    #NEW and "imporved" intitailizatioon from hash
    def __init__(self, hash):
        self.id = hashingVals.hashback.get(hash[0])
        self.len = int(hash[1])
        self.wid = int(hash[2])
        
        self.shape = []
        self.shapeN = []
        
        self.h = hash
        self.mult = []
        self.allPos = []
        
        self.number = hash[3:]
        for i in range(self.wid):
            bin = dec_to_bin_zeros(hashingVals.hashback.get(hash[3+i]), self.len)
            self.shape.append([k for k in bin])
            self.shapeN.append(hashingVals.hashback.get(( hash[3+i]) ))

    def __str__(self):
        col = colorNums.colors[self.id]
        black = bcolors.Black
        ret = "\n"
#        ret += str(self.id)
#        ret += col
#        ret += f'len : {self.len}\nwid : {self.wid}\n'
        for i in self.shapeN:
            ret += str(i)
            ret += " "
        ret += "\n"
        for row in self.shape:
           # print(type(row))
            for i in row:
                if i == '0':
                    ret += black
                    ret += '.'
                else:
                    ret += col
                    ret += '*'
#                ret += i
            ret += "\n"
#        for i in self.shape[-1]:
#            ret += col
#            ret += '*'
#            ret += i
        ret += bcolors.ResetAll
        
        ret += "HASH: "
        ret += self.h
#        ret += "\n"
#        ret += str(self.mult)
        return ret
        
    def __eq__(self,obj):
        return isinstance(obj,Pentamino) and self.shape == obj.shape
        
    #Go hashing.txt to get a full walk through of how we hash Pentaminos
    def __hash__(self):
        #Checkes if id is greater than 9
        if ( self.id > 9):
            h1 = str(hashingVals.hashes.get(self.id))
        else:
            h1 = str(self.id)
        h1 += str(self.len) + str(self.wid)
        bin  = ''
        #loop through all rows of the penatmino
        for row in self.shape:
            #adds the hash of the rows 0's and 1's in binary to h
            for i in row:
                bin += i
            
            h = int(bin, base=2)
            
            if ( h > 9 ):
                h1 += hashingVals.hashes.get(h)
            else:
                h1 += str(h)
            bin = ''
        return hash(h1)
        
    def __lt__(self,other):
        return self.id < other.id
    
    
        
    #@returns h1 : returns the hash value we generate to give to the hash() function
    def gethash(self):
        #Checkes if id is greater than 9
        if ( self.id > 9):
            h1 = str(hashingVals.hashes.get(self.id))
        else:
            h1 = str(self.id)
        h1 += str(self.len) + str(self.wid)
        bin  = ''
        #loop through all rows of the penatmino
        for row in self.shape:
            #adds the hash of the rows 0's and 1's in binary to h
            for i in row:
                bin += i
            #Checkes if values is greater than 9
            if ( int(bin,base=2) > 9 ):
                h1 += hashingVals.hashes.get(int(bin,base=2))
            else:
                h1 += str(int(bin,base=2))
#            print(f'h: {h} bin: {bin} ')
            bin = ''
#        print(f'{h1}')
      #  print(f' h1 hashed:  {hash(h1)}')
        return h1
#

    def getPositions(self, size):
        for i in range(len(self.shape)):
            self.shape[i].append(0)
        self.shape.append([0 for j in range(size) for i in range(5-self.wid)])
        print(self.shape)


#Class to hold all varations of a penta
class PentaContainer:
    def __init__(self, _pentas):
        self.pentas = _pentas
        self.id = self.pentas[0].id
        self.Full = []
        self.BinFull = []
        
    def __str__(self):
        ret = ''
        for i in self.pentas:
            ret += str(i)
        return ret
        
    def BinString(self):
       
        ret = 'hello\n'
        for a in range(len(self.BinFull)):
            print(a,self.BinFull[a])
            for b in range(len(self.BinFull[a])):
                if b % 5 == 0 and b != 0:
                    ret += '\n'
#                    print()
#                print(str(self.BinFull[a][b]),end= ' ')
                ret += str(self.BinFull[a][b])
            ret += '\n\n'
#            print('\n')
        return ret
            
        
class board:
    def __init__(self,_size,_pentas):
        self.size = _size
        self.pentas = _pentas
        self.all = []
        self.allmult = []
        self.board = [[0 for j in range(_size)]for i in range(5)]
        
        
    def __str__(self):
        ret = "+"
        ret += "---+" * self.size
        ret += "\n"
        for i in range(len(self.board)):
            ret +="|"
            for j in range(len(self.board[i])):
                ret += ' ' + str(self.board[i][j]) +' |'
            ret += "\n"
        ret += "+"
        ret += "---+" * self.size
        ret += "\n"
        
#        ret += str(self.board)
#        ret += "\n"
        
        for p in self.pentas:
            ret += str(p)

#
        return ret

    def notSolved(self):
        for row in self.board:
            for i in row:
                if i != 1:
                    return True
        return False


    def solve(self):
        print("SOLVING")
    
        #the xy cordinates of each of the pentaminoes
        pos_x = [0 for i in range(self.size)]
        pos_y = [0 for i in range(self.size)]
        
        #the iteration of the pentamino
        currIter = [0 for i in range(self.size)]
        
#        for curp


        for c in range(len(self.pentas)):
            #loop through all iterations of the Pentamino
            for i in range(len(self.pentas[c].pentas)):
                self.board = [[0 for j in range(self.size)]for i in range(5)]
                #loop through all pentaminos
                print(currIter)
                for p in range(len(self.pentas[:1])):
                    print( self.pentas[p].pentas[currIter[p]])
                    #loop through the shape of the current pentamino
                    for x in range(self.pentas[p].pentas[currIter[p]].wid):
                        for y in range(self.pentas[p].pentas[currIter[p]].len):
    #                        print(f'x: {x} y: {y}')
    #                        print(f'pos_x[p]+x {pos_x[p]+x} pos_y[p]+y {pos_y[p]+y}')
        #                       print(len(self.board))
        
                            #if the current position is outside the bounds of the board dont place
                            if ((pos_x[p]+x) > 5 or (pos_y[p]+y) > self.size-1 ):
                                pass
                            #if the current position exists in the bounds of the board then place
                            else:
                                self.board[pos_x[p]+x][pos_y[p]+y] += int(self.pentas[p].pentas[currIter[p]].shape[x][y])
        #                        print(self.pentas[p].pentas[currIter[p]])
                
                currIter[c] += 1
                print(self)
            currIter[c] = 0
            
        
        
#            print(self.pentas[p].pentas[currIter[p]])
#            print(self.pentas[p].pentas[currIter[p]].len)

         
    def solve2 (self):
        currIter = [0 for i in range(self.size)]
        
        for p in self.pentas:
            for i in p.pentas:
                print(i.h)
                print(currIter)
                
     
    #@param allSol : a Boolean that is true for all solutions, and false for the first solutioon found
    #@returns
    def binSolver (self,allSol):
        
#        print(f'{self.pentas[p]}\nFULL: {self.pentas[p].Full}')

        for p in  range(len(self.pentas)):
            self.all.append(self.pentas[p].Full)
            
#        for a in self.all:
#            for b in a:
#                print (f'all {b}')
            
        for element in itertools.product(*self.all):
            self.allmult.append(list(element))
   
#        for m  in self.allmult:
#            for n in m:
#                print (f'allmult {n}')
#            print("\n")
            
        allSums = []
        
        for a in self.allmult:
            for element in itertools.product(*a):
                for e in itertools.product(*element):
#                    print(e)
                    Fit = True
                    sums = [0 for i in range(5)]
                    for x in range(len(e)):
                        for y in range(len(e[x])):
                            sums[y] += e[x][y]
                            if( sums[y] > ((2 ** self.size)-1 ) ):
                                Fit = False
                                break
#                        print(e[x])
#                    print()
                    
                    
                    if binary.checker(sums, (2 ** self.size)-1):
                        allSums.append(e)
                        if (not allSol):
                        
                            print('First Solution found: ')
                            print( ('+' + '---' * self.size +'--+   ') * self.size +  '| ROW SUM ')
                            rows = [[] for _ in range(5)]
            #                print(allSums[a])
                            for b in range(len(e)):
            #                    print(allSums[a][b])
                                for c in range(5):
                                    rows[c].append( dec_to_bin_zeros(e[b][c],self.size ) )
            #                    print(b)
                            counter = 0
                            for a in rows:
                                print('|',end=' ')
                                for b in range(len(a)) :
                                    col = colorNums.colors[b]
                                    black = bcolors.Black
                                    reset  =  bcolors.ResetAll
                                    for c in range(len(a[b])):
                                        if a[b][c] == '0':
                                            print(black,'.',end=' ')
                                        else:
                                            print(col,'*',end=' ')
                                    print(reset,'|   | ',end ='')
                                print((2**self.size)-1)
            #                print(rows)
                            print(bcolors.ResetAll,end='')
                            print( ('+' + '---' * self.size +'--+   ') * self.size)
                            
                            
                            return True
                            
                    elif Fit:
                        pass
#                        print(f' sums :{sums} {e}')
                    else:
                        pass
#                        print("FAIL")
#                        print(f'  sums :{sums} {element}')
           
           
        if len(allSums) == 0:
            return False
#            print('no solutions found')
        else:
            print('SOLUTIONS: ')
            
            
            for x in range(len(allSums)):
                print( ('+' + '---' * self.size +'--+\t') * self.size + '| ROW SUM ' )
                rows = [[] for _ in range(5)]
#                print(allSums[a])
                for b in range(len(allSums[x])):
#                    print(allSums[a][b])
                    for c in range(5):
                        rows[c].append( dec_to_bin_zeros(allSums[x][b][c],self.size ) )
#                    print(b)
                for a in rows:
                    print('|',end=' ')
                    for b in range(len(a)) :
                        col = colorNums.colors[b]
                        black = bcolors.Black
                        reset  =  bcolors.ResetAll
                        for c in range(len(a[b])):
                            if a[b][c] == '0':
                                print(black,'.',end=' ')
                            else:
                                print(col,'*',end=' ')
                        print(reset,'|   | ',end ='')
                    print((2**self.size)-1)
                
                    
#                print(rows)
                print( ('+' + '---' * self.size +'--+\t') * self.size)
                print(bcolors.ResetAll,end='')
#                print(f'solution #{a}: {int(bin(allSums[a])[2:])} ')
          
            return True
        
            
#                print(element)
#                for e in element:
#                    print(e)
#                print()
                
   
#        print(((2 ** int(self.size))-1 ))

    #@param dups Boolean, True means the same Pentamino can be used more than once in a solution, false means all pentaminos must be used in all solutions
    #@param printing Boolean, True means we will output the solutions, False means no output
    def dancinglinks(self,dups,printing):
        X = {f for f in range(self.size*5)}
#        print(X)
        X = {j: set() for j in X}
#        print(X)
        
        for p in  range(len(self.pentas)):
            self.all.append(self.pentas[p].BinFull)
#            print(self.pentas[p])
#            self.pentas[p].BinString()
            
            
        Y = {}
            
        for a in range(len(self.all)):
            for b in range(len(self.all[a])):
#                print(a,b,self.all[a][b])
                indices = [i for i, x in enumerate(self.all[a][b]) if x == 1]
#                print(indices)
                Y[str(a)+","+str(b)] = indices
        
#        for key, value in Y.items():
#            print(key,value)
        
        for i in Y:
            for j in Y[i]:
                pass
#                print(j)
                X[j].add(i)
                
#        for key, value in X.items():
#            print(key,value)
        
        solution = []
        solutions = Kunths.solve(X, Y, solution)
        
        
        if(dups):
#            print('SOLUTIONS with dups:')
            solsBin = []
            for a in solutions:
                curr_sol = []
                for b in a:
                    ind = b.split(',')
                    sol = self.all[int(ind[0])][int(ind[1])]
                    curr_sol.append(sol)
                solsBin.append(curr_sol[:])
        else:
#           print('SOLUTIONS without dups:')
            solsBin = []
            pieces = []
            for a in solutions:
                curr_sol = []
                curP = []
                
                curr_pieces = set()
                for b in a:
                    ind = b.split(',')
                    curP.append(ind)
                    
                    
                    curr_pieces.add(ind[0])
                    sol = self.all[int(ind[0])][int(ind[1])]
                    curr_sol.append(sol)
                if len(curr_pieces) == self.size:
                    solsBin.append(curr_sol[:])
                    pieces.append(curP)
            
        if(len(solsBin) != 0):
            if(printing):
        
                print('\nSolutions\n')
    #            for p in pieces:
    #                for q in p:
    #                    print(self.pentas[int(q[0])])
    #            print(pieces)
            
            
                solNum = itertools.count()
                for a in solsBin:
            #           print(a)
                    print(f'Solution {next(solNum)}:')
                    print( ('+' + '---' * self.size +'--+   ') * self.size)
                    rows = [[] for _ in range(5)]
                    for b in a:
                        for c in range(len(b)):
            #                   print(b[c],end =" ")
                            rows[c//self.size].append(b[c])
            #               print()
                    for b in rows:
                        print('| ',end='')
                        for c in range(len(b)):
                            col = colorNums.colors[c//self.size]
                            black = bcolors.Black
                            reset  =  bcolors.ResetAll
                            if c % self.size == 0 and c != 0:
                                print(reset,'|   | ',end ='')
                            if b[c] == 0:
                                print(black,'.',end=' ')
                            else:
                                print(col,'*',end=' ')
                        print(reset,'| ',end='')
                        print(reset)

                    print( ('+' + '---' * self.size +'--+   ') * self.size)
                    print(bcolors.ResetAll,end='')

            return True
        return False
    





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
    
def rotate (pentamino):
    """function to rotate a shape 90 deg CW"""
    lengthy = int(pentamino.wid) 
    lengthx = int(pentamino.len)

    newshape = [[ 0 for j in range(lengthy) ]for i in range(lengthx)]
    
    for x in range(0,lengthx):
        for y in range(0,lengthy):
            newshape[x][y] = pentamino.shape[lengthy-y-1][x]     
    return Pentamino(newshape,pentamino.id)

def transpose (pentamino):
    """determine transpose"""
    leny = int(pentamino.wid)
    lenx = int(pentamino.len)
    news = [[0 for j in range(leny)]for i in range(lenx)]

    for x in range(0, lenx):
        for y in range(0, leny):
            news[x][y] = pentamino.shape[y][x]
            
    return Pentamino(news,pentamino.id)

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
    
#@param allIters: Set of Pentamino objects
#@returns allDict: Dictionary Object
#                  -keys = all pentamino id's which appear in allIters
#                   -values = all Pentaminos in allIters with an id matching that matches the key
def generateAllDict(allIters):
    allDict = {}
    for i in allIters:
        if i.id in allDict.keys():
            allDict[i.id].append(i)
        else:
            allDict[i.id] = [i]
    return allDict


#@param filename : filename we are reading in 'hashedPentas.txt'
#@returns allPentas: Array of all pentaminoes
def getPentasFromHash(filename):
    #opens file and reads it line by line
    with open(filename,'r') as myfile:
        data = myfile.read().splitlines()
    #Varibables
    allPentas = []
    penta = []
    #loop through all lines in .txt file
    for d in data:
        allPentas.append(Pentamino(d))
    return allPentas

#@param allDict: Dictionary Object
#                  -keys = all pentamino id's
#                   -values = all iterations of the Pentamino with an id matching that matches the key
#@returns Pentas: list of PentaContainer class objects
def DictToPentas(allDict):
    Pentas = []
    for key,value in sorted(allDict.items()):
#        print(f'Pentanmino ID: {key} ')
        Pentas.append(PentaContainer(value))
    return Pentas
 
 


def main():
    DEBUG = 0

#    allPentas = getPentas('Pentamino.txt')

#    #list of all pentamino objects
#    allPC = []
#    x = 0
#    for i in allPentas:
#        allPC.append(Pentamino(i,x))
#        x += 1
#
    
#    #All possible iterations of all Pentaminoes
#    allIters = generateAllIters(allPC)
#    print("Set of all pentaminoes variations")
#    for i in sorted(allIters):
#        print(i)
#        print(f'HASH VALUE: {i.gethash()}')

    #Getting Pentamios from hashees:
    allPentas = getPentasFromHash('hashedPentas.txt')
    
    
    if(DEBUG):
        for i in allPentas:
            #Checking if hashvalues match what is expected
            print(f' input hash: {i.h} calculated hash {i.gethash()} \t MATCH {i.h==i.gethash()}')
#            print(i)


    allDict = generateAllDict(allPentas)
    if(DEBUG):
        print("JUICY Dictionary")
        for key,value in sorted(allDict.items()):
    #        print(f'Pentanmino ID: {key} ')
            for i in value:
                print(i)

#        print(allDict)
    
    allPents = DictToPentas(allDict)

    if(DEBUG):
        numFixed = 0
        for p in allPents:
            numFixed += len(p.pentas)
#            print(p)
        print(f'Number of fixed pentaminoes: {numFixed} \nNumber of free pentaminoes:  {len(allPents)}')
    
    #################################################
    #################################################
    BOARD_SIZE = 4 #<--- Change to maximum board size
    #################################################
    #################################################
    
    #Loop through all Pents calculate all their positions
    cop = 0
    for p in range(len(allPents)):
        for q in range(len(allPents[p].pentas)):
            cop += 1
            allPents[p].pentas[q].mult = binary.multiplyList(allPents[p].pentas[q].shapeN,BOARD_SIZE)
            for m in allPents[p].pentas[q].mult:
                allPents[p].pentas[q].allPos.append(binary.addzeros(m,5))
            if(DEBUG):
                print(f'{cop}: \t{allPents[p].pentas[q].mult} \n\t{allPents[p].pentas[q].allPos} ')
  
    x = 0
    for p in range(len(allPents)):
        for q in range(len(allPents[p].pentas)):
#                print(self.pentas[p].pentas[q])
#                print(self.pentas[p].pentas[q].allPos)
                allPents[p].Full.append((allPents[p].pentas[q].allPos))
                
    for p in range(len(allPents)):
#        print(allPents[p])
        for f in range(len(allPents[p].Full)):
#            print(allPents[p].Full[f])
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
                    
                            
    if(DEBUG):
        for p in range(len(allPents)):
            print(allPents[p])
            for r in range(len( allPents[p].BinFull)):
                print(allPents[p].BinFull[r])
            print()
    
    
            
###TEST WITH 1
#    print(allPents[4])
#    one = board(1,[allPents[4]])
#    print(one)
#    one.binSolver(1)
#    one.dancinglinks(1)

####TEST WITH 3
#    b = board(3,[allPents[4],allPents[5],allPents[11]])
#    b.binSolver(1)
#    b.dancinglinks(0,1)
    
    
######TEST WITH 4
#    b = board(4,[allPents[4],allPents[5],allPents[11],allPents[1]])
#    b.binSolver(0)
#    b.dancinglinks(0,1)
    
#####TEST WITH 5
#    b = board(5,[allPents[4],allPents[5],allPents[11],allPents[1],allPents[3]])
##    print(b.pentas[0].pentas[0])
#    b.binSolver(0)
    
##TEST WITH 6
#    b = board(6,[allPents[4],allPents[5],allPents[11],allPents[1],allPents[3],allPents[9]])
#    b.binSolver(0)

#    print(b)

##TEST WITH all possible 3
#    allThree = list(itertools.combinations(allPents,3))
#    for a in range(len(allThree)):
#        b = board(3,list(allThree[a])[:])
#        b.binSolver(1)
##TEST WITH all possible 4
#    allThree = list(itertools.combinations(allPents,4))
#    for a in range(len(allThree)):
#        b = board(4,list(allThree[a])[:])
#        b.binSolver(0)
##TEST WITH all possible 5
#    allThree = list(itertools.combinations(allPents,5))
#    for a in range(len(allThree)):
#        b = board(5,list(allThree[a])[:])
#        b.binSolver(0)

#TEST WITH 12
#    allThree = list(itertools.combinations(allPents,5))
#    for a in range(len(allThree)):
#        b = board(12,list(allThree[a])[:])
#        b.binSolver(0)


##DANCING TESTING---------------------------------
##TEST WITH all possible 3
#    testing.testAll3iter(allPents)
#    testing.testAll3(allPents)
    
    testing.testAll(allPents,BOARD_SIZE)
    
    
    
#    b = board(5,allPents)
#    b.dancinglinks(1)
    
#Small Slam A
#Executions time: 126.77 seconds
#    b = board(8,[allPents[4],allPents[5],allPents[11],allPents[1],allPents[3],allPents[9],allPents[8],allPents[0]])
#    b.dancinglinks(0)
#
    
#    testing.testAll4x2(allPents)
#    testing.testAll5x2(allPents)
#    testing.testAll6x2(allPents)
     
     
     
#    b = board(12,allPents)
#    b.dancinglinks(0,1)
#
     
#    for a in sol:
#        LOS.append(set())
#        for b in a:
#            print(b.id,end = ' ')
#        print()
#
#    print(LOS)
    
    
    
#    b = board(4,allPents)
#    b.dancinglinks(0)

#Penta 9 A

#    b = board(9,[allPents[6],allPents[4],allPents[5],allPents[0],allPents[8],allPents[1],allPents[2],allPents[9],allPents[7]])
#    b.dancinglinks(0)


#    allPents[4].pentas[0].getPositions(3)

#    b.solve2()
#    print(b)
    

if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f'Executions time: {round(end - start,2)} seconds')
