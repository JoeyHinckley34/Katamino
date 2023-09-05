from colors_util import bcolors, colorNums
from hashing_util import BinConvert, hashingVals

#Old Pentamino implementation
class Pentamino:
    def __init__(self, _shape, _id):
        self.shape = _shape
        self.id = _id
        self.len = len(self.shape[0])
        self.wid = len(self.shape)
#        self.shapes =

    def __str__(self):
        col = colorNums.colors[self.id]
        black = bcolors.Black
        ret = ""
        ret += col
        ret = "-\n"
        for row in self.shape:
            for i in row:
                if i == '0':
                    ret += black
                    ret += '.'
                else:
                    ret += col
                    ret += '*'
#                ret += i
            ret += "\n"
        ret += bcolors.ResetAll
        return ret

    def __lt__(self,other):
        return self.id < other.id
        
    #@returns h1 : returns the hash value we generate to give to the hash() function
    def gethash(self):
        #Checkes if id is greater than 9
        if (self.id > 9):
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
