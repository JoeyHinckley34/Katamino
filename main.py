import numpy as np
import binary
import itertools

class bcolors:
    ResetAll = "\033[0m"

    Bold       = "\033[1m"
    Dim        = "\033[2m"
    Underlined = "\033[4m"
    Blink      = "\033[5m"
    Reverse    = "\033[7m"
    Hidden     = "\033[8m"

    ResetBold       = "\033[21m"
    ResetDim        = "\033[22m"
    ResetUnderlined = "\033[24m"
    ResetBlink      = "\033[25m"
    ResetReverse    = "\033[27m"
    ResetHidden     = "\033[28m"

    Default      = "\033[39m"
    Black        = "\033[30m"
    Red          = "\033[31m"
    Green        = "\033[32m"
    Yellow       = "\033[33m"
    Blue         = "\033[34m"
    Magenta      = "\033[35m"
    Cyan         = "\033[36m"
    LightGray    = "\033[37m"
    DarkGray     = "\033[90m"
    LightRed     = "\033[91m"
    LightGreen   = "\033[92m"
    LightYellow  = "\033[93m"
    LightBlue    = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan    = "\033[96m"
    White        = "\033[97m"

    BackgroundDefault      = "\033[49m"
    BackgroundBlack        = "\033[40m"
    BackgroundRed          = "\033[41m"
    BackgroundGreen        = "\033[42m"
    BackgroundYellow       = "\033[43m"
    BackgroundBlue         = "\033[44m"
    BackgroundMagenta      = "\033[45m"
    BackgroundCyan         = "\033[46m"
    BackgroundLightGray    = "\033[47m"
    BackgroundDarkGray     = "\033[100m"
    BackgroundLightRed     = "\033[101m"
    BackgroundLightGreen   = "\033[102m"
    BackgroundLightYellow  = "\033[103m"
    BackgroundLightBlue    = "\033[104m"
    BackgroundLightMagenta = "\033[105m"
    BackgroundLightCyan    = "\033[106m"
    BackgroundWhite        = "\033[107m"

class colorNums:
    colors = [  bcolors.Blue,
                bcolors.Magenta,
                bcolors.Yellow,
                bcolors.Green,
                bcolors.Red,
                bcolors.LightGray,
                bcolors.Cyan,
                bcolors.DarkGray,
                bcolors.LightCyan,
                bcolors.LightMagenta,
                bcolors.LightRed,
                bcolors.LightGreen,
            ]

class BinConvert:
    toBinary1 =  {  0 : '0',
                    1 : '1'
                }

    toBinary2 = {   0 : '00',
                    1 : '01',
                    2 : '10',
                    3 : '11'
                }
    toBinary3 = {   0 : '000',
                    1 : '001',
                    2 : '010',
                    3 : '011',
                    4 : '100',
                    5 : '101',
                    6 : '110',
                    7 : '111'
                }
    
    toBinary4 = {   0 : '0000',
                    1 : '0001',
                    2 : '0010',
                    3 : '0011',
                    4 : '0100',
                    5 : '0101',
                    6 : '0110',
                    7 : '0111',
                    8 : '1000',
                    9 : '1001',
                    10 : '1010',
                    11 : '1011',
                    12 : '1100',
                    13 : '1101',
                    14 : '1110',
                    15 : '1111'
                }
    toBinary5 = {   0 : '00000',
                    1 : '00001',
                    2 : '00010',
                    3 : '00011',
                    4 : '00100',
                    5 : '00101',
                    6 : '00110',
                    7 : '00111',
                    8 : '01000',
                    9 : '01001',
                    10 : '01010',
                    11 : '01011',
                    12 : '01100',
                    13 : '01101',
                    14 : '01110',
                    15 : '01111',
                    16 : '10000',
                    17 : '10001',
                    18 : '10010',
                    19 : '10011',
                    20 : '10100',
                    21 : '10101',
                    22 : '10110',
                    23 : '10111',
                    24 : '11000',
                    25 : '11001',
                    26 : '11010',
                    27 : '11011',
                    28 : '11100',
                    29 : '11101',
                    30 : '11110',
                    31 : '11111'
                }





class hashingVals:
    hashes = {  10 : 'a',
                11 : 'b',
                12 : 'c',
                13 : 'd',
                14 : 'e',
                15 : 'f',
                31 : 'g'
            }
            
    hashback =  {   '0' : 0,
                    '1' : 1,
                    '2' : 2,
                    '3' : 3,
                    '4' : 4,
                    '5' : 5,
                    '6' : 6,
                    '7' : 7,
                    '8' : 8,
                    '9' : 9,
                    'a' : 10,
                    'b' : 11,
                    'c' : 12,
                    'd' : 13,
                    'e' : 14,
                    'f' : 15,
                    'g' : 31
                }

def dec_to_bin(x):
    return int(bin(x)[2:])

def dec_to_bin_zeros(x,z):
    return f'{int(bin(x)[2:]):03}'



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
            if(self.len == 1 ):
                bin = BinConvert.toBinary1.get( hashingVals.hashback.get(hash[3+i]))
                self.shape.append([k for k in bin])
                self.shapeN.append(hashingVals.hashback.get(( hash[3+i]) ))
            elif(self.len == 2 ):
                bin = BinConvert.toBinary2.get( hashingVals.hashback.get(hash[3+i]))
                self.shape.append([k for k in bin])
                self.shapeN.append(hashingVals.hashback.get(( hash[3+i]) ))
            elif(self.len == 3 ):
                bin = BinConvert.toBinary3.get( hashingVals.hashback.get(hash[3+i]))
                self.shape.append([k for k in bin])
                self.shapeN.append(hashingVals.hashback.get(( hash[3+i]) ))
            elif(self.len == 4 ):
                bin = BinConvert.toBinary4.get( hashingVals.hashback.get(hash[3+i]))
                self.shape.append([k for k in bin])
                self.shapeN.append(hashingVals.hashback.get(( hash[3+i]) ))
            elif(self.len == 5 ):
                bin = BinConvert.toBinary5.get( hashingVals.hashback.get(hash[3+i]))
                self.shape.append([k for k in bin])
                self.shapeN.append(hashingVals.hashback.get(( hash[3+i]) ))
            else :
                self.shape = "FAIL!!"
            
    
        
#   OLD LAME INIT Gross !
#    def __init__(self, _shape, _id):
#        self.shape = _shape
#        self.id = _id
#        self.len = len(self.shape[0])
#        self.wid = len(self.shape)

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
        self.Full = []

    def __str__(self):
        ret = ''
        
        for i in self.pentas:
            ret += str(i)
        
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
        ret += str(self.board)
        ret += "\n"
        
        
        
#        for p in self.pentas:
#            ret += str(p)
#
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
                            print(e)
                            return
                            
                    elif Fit:
                        pass
#                        print(f' sums :{sums} {e}')
                    else:
                        pass
#                        print("FAIL")
#                        print(f'  sums :{sums} {element}')
           
           
        if len(allSums) == 0:
            print('no solutions found')
        else:
            print('SOLUTIONS: ')
            
           
            
            for a in range(len(allSums)):
                rows = [[] for _ in range(5)]
#                print(allSums[a])
                for b in range(len(allSums[a])):
#                    print(allSums[a][b])
                    for c in range(5):
                        rows[c].append( dec_to_bin_zeros(allSums[a][b][c],3 ) )
#                    print(b)
                for a in rows:
                    for b in a  :
                        for c in b:
                            if c == '0':
                                print('.',end=' ')
                            else:
                                print('*',end=' ')
                        print('\t',end ='')
                    print()
#                print(rows)
                print()
#                print(f'solution #{a}: {int(bin(allSums[a])[2:])} ')
          
            
        
            
#                print(element)
#                for e in element:
#                    print(e)
#                print()
                
   
#        print(((2 ** int(self.size))-1 ))


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
    
    
    
    #Loop through all Pents calculate their
    cop = 0
    for p in range(len(allPents)):
        for q in range(len(allPents[p].pentas)):
            cop += 1
            allPents[p].pentas[q].mult = binary.multiplyList(allPents[p].pentas[q].shapeN,3) #<--- Change to maximum board size
            for m in allPents[p].pentas[q].mult:
                allPents[p].pentas[q].allPos.append(binary.addzeros(m,5))
            if(DEBUG):
          
                print(f'{cop}: \t{allPents[p].pentas[q].mult} \n\t{allPents[p].pentas[q].allPos} ')
  
    for p in range(len(allPents)):
        for q in range(len(allPents[p].pentas)):
#                print(self.pentas[p].pentas[q])
#                print(self.pentas[p].pentas[q].allPos)
                allPents[p].Full.append((allPents[p].pentas[q].allPos))
            
  
####TEST WITH 1
#    print(allPents[4])
    one = board(1,[allPents[4]])
#    print(one)
#    one.binSolver(1)

####TEST WITH 3
    b = board(3,[allPents[4],allPents[5],allPents[11]])
    b.binSolver(1)
    
######TEST WITH 4
    b = board(4,[allPents[4],allPents[5],allPents[11],allPents[1]])
#    b.binSolver(0)

#####TEST WITH 5
#    b = board(5,[allPents[4],allPents[5],allPents[11],allPents[1],allPents[3]])
##    print(b.pentas[0].pentas[0])
#    b.binSolver(0)
    
##TEST WITH 6
#    b = board(6,[allPents[4],allPents[5],allPents[11],allPents[1],allPents[3],allPents[9]])
#    b.binSolver(0)

#    print(b)


#    allPents[4].pentas[0].getPositions(3)

#    b.solve2()
#    print(b)
    

if __name__ == '__main__':
    main()
