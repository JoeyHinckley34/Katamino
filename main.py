
import numpy as np
import time as t

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
        
        
class board:
    def __init__(self,_size,_pentas):
        self.size = _size
        self.pentas = _pentas
        self.history = []
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
        #ret += str(self.board)
        return ret
    
    def solve(self):

        x = 0
        y = 0
        for i in range(len(self.pentas)):
            print("Now on shape: ", i, "\n", self.pentas[i])
            
            found = False
            while (y < len(self.board)):
                #print("top: ", i, x, y)
                #print(x, y)
                ret = self.place(self.pentas[i], x, y)
                if (ret):
                    #valid place
                    #put into history
                    print(i)
                    self.history.append((self.pentas[i], x, y))
                    found = True
                    print("PLACED: ", x, y)
                    x = 0
                    y = 0
                    break
                else:
                    if (x == len(self.board[0])): #might be board[0]
                        x = 0
                        y += 1
                    else:
                        x += 1
                
            #break
            #no valid position, backtrack through history.
            if not found:
                print("backtrack")
                i -= 1
                prev = self.history.pop(-1)
                self.pentas[i] = transpose(prev[0])

        return False

    def place(self, piece, x, y):
        #returns true on successfull place

        #print(piece.shape)
        for i in range(len(piece.shape)):
            for j in range(len(piece.shape[i])):
                #print(x + i, j + y, len(self.board))
                if ((x + i < 0 or j + y < 0) or (x + i >= len(self.board) or j + y >= len(self.board[0]))):
                    #print("OOB")
                    return False
                
                elif (self.board[i + x][j + y] != 0):
                    #print("Collision:")
                    return False

        for i in range(len(piece.shape)):
            for j in range(len(piece.shape[i])):
                if (piece.shape[i][j] == '1'):
                    #print(i, j, x, y)
                    self.board[i + x][j + y] = piece.id

        return True
    
    


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

    b = board(4,[allPC[4],allPC[5],allPC[11]])
    b.solve()
    print("FINISHED BOARD:::")
    print(b)


if __name__ == '__main__':
    main()
