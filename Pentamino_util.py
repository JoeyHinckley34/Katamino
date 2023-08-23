from colors_util import bcolors, colorNums
from hashing_util import BinConvert, hashingVals
from helper_functions import dec_to_bin, dec_to_bin_zeros

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
            
    def __lt__(self,other):
        return self.id < other.id

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

    def __eq__(self,obj):
        return isinstance(obj,Pentamino) and self.id == obj.id
            
    def __lt__(self,other):
        return self.id < other.id
            
