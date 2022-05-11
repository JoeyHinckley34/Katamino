import numpy as np


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

class hashingVals:
    hashes = {  10 : 'a',
                11 : 'b',
                12 : 'c',
                13 : 'd',
                14 : 'e',
                15 : 'f',
                31 : '0'
            }

class Pentamino:
    def __init__(self, _shape, _id):
        self.shape = _shape
        self.id = _id
        self.len = len(self.shape[0])
        self.wid = len(self.shape)
#        self.shapes =

#    def __init__(self, hash):
        

    def __str__(self):
        col = colorNums.colors[self.id]
        black = bcolors.Black
        ret = "-\n"
#        ret += col
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
#        ret += self.hash()
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
class board:
    def __init__(self,_size,_pentas):
        self.size = _size
        self.pentas = _pentas
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
        for p in self.pentas:
            ret += str(p)
        return ret
    


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

def main():
    #list of all pentaminoes
    #3d array
    allPentas = getPentas('Pentamino.txt')
    #list of all pentamino objects
    allPC = []
    x = 0
    for i in allPentas:
        allPC.append(Pentamino(i,x))
        x += 1
    
    
    


#
#    for i in allPC:
#        print(i)

#  c  b = board(4,[allPC[4],allPC[5],allPC[11]])
    #print(b)
    
#    for i in b.pentas:
#        print(i)
#
    
    
    #All possible iterations of all Pentaminoes
    allIters = generateAllIters(allPC)
    
#    print("Set of all pentaminoes variations")
#    for i in sorted(allIters):
#        print(i)
#        print(f'HASH VALUE: {i.gethash()}')
#
        
    allDict = generateAllDict(allIters)
#    print("JUICY Dictionary")
    for key,value in sorted(allDict.items()):

#        print(f'Pentanmino ID: {key} ')
        for i in value:
#            print(i)
            print(i.gethash())
#            print(hash(i))

    

if __name__ == '__main__':
    main()
