import Kunths
import itertools
import binary
from colors_util import bcolors, colorNums
from hashing_util import BinConvert, hashingVals
from Pentamino_util import Pentamino, PentaContainer
from helper_functions import dec_to_bin_zeros

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
        for p in self.pentas:
            ret += str(p)
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
            print('No solutions found')
            return False
        else:
            print('SOLUTIONS: ')
            
            for x in range(len(allSums)):
                print( ('+' + '---' * self.size +'--+   ') * self.size + '| ROW SUM ' )
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
                print( ('+' + '---' * self.size +'--+   ') * self.size)
                print(bcolors.ResetAll,end='')
#                print(f'solution #{a}: {int(bin(allSums[a])[2:])} ')
          
            return True
        
            
#                print(element)
#                for e in element:
#                    print(e)
#                print()
                
   
#        print(((2 ** int(self.size))-1 ))

    #@param dups 0-2,   0 means all pentaminos must be used in all solutions
    #                   1 means the same Pentamino can be used more than once in a solution,
    #                   2 means only one Pentamino can be used in the solutions
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
        
        
        if(dups==1):
#            print('SOLUTIONS with dups:')
            solsBin = []
            for a in solutions:
                curr_sol = []
                for b in a:
                    ind = b.split(',')
                    sol = self.all[int(ind[0])][int(ind[1])]
                    curr_sol.append(sol)
                solsBin.append(curr_sol[:])
        elif(dups == 2):
            print('SOLUTIONS with one tile:')
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
                if len(curr_pieces) == 1:
                    solsBin.append(curr_sol[:])
                    pieces.append(curP)
            
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
    