import itertools
from main import board

#####################
#Dancing Links Tests#
#####################

#Solutions of 2 4x5s without duplicates
def testAll4x2(allPents):
    sol = []
    allFour = list(itertools.combinations(allPents,4))
    for a in range(len(allFour)):
        b = board(4,list(allFour[a])[:])
        if(b.dancinglinks(0,0)):
            sol.append(allFour[a][:])
    ALLp = []
    lst = list(itertools.combinations(sol,2))
    for a in lst:
        p = []
        for b in a:
            for c in b:
                p.append(c.id)
        if len(set(p)) == 8:
            ALLp.append(p)
    for a in ALLp:
        print('NEW SOLUTION')
        b = board(4,[allPents[x] for x in a[0:4] ])
        b.dancinglinks(0,1)
        b = board(4,[allPents[x] for x in a[4:] ])
        b.dancinglinks(0,1)

#Solutions of 2 5x5s without duplicates
#Executions time: 44.39 seconds
def testAll5x2(allPents):
    sol = []
    allFour = list(itertools.combinations(allPents,5))
    for a in range(len(allFour)):
        b = board(5,list(allFour[a])[:])
        if(b.dancinglinks(0,0)):
            sol.append(allFour[a][:])
    ALLp = []
    lst = list(itertools.combinations(sol,2))
    for a in lst:
        p = []
        for b in a:
            for c in b:
                p.append(c.id)
        if len(set(p)) == 10:
            ALLp.append(p)
    for a in ALLp:
        print('NEW SOLUTION')
        b = board(5,[allPents[x] for x in a[0:5] ])
        b.dancinglinks(0,1)
        b = board(5,[allPents[x] for x in a[5:] ])
        b.dancinglinks(0,1)
    
# Solutions of 2 6x5s without duplicates
#Executions time: 458.24 seconds
def testAll6x2(allPents):
    sol = []
    allFour = list(itertools.combinations(allPents,6))
    for a in range(len(allFour)):
        b = board(6,list(allFour[a])[:])
        if(b.dancinglinks(0,1)):
            sol.append(allFour[a][:])
    ALLp = []
    lst = list(itertools.combinations(sol,2))
    for a in lst:
        p = []
        for b in a:
            for c in b:
                p.append(c.id)
        if len(set(p)) == 12:
            ALLp.append(p)
    for a in ALLp:
        print('NEW SOLUTION')
        b = board(6,[allPents[x] for x in a[0:6] ])
        b.dancinglinks(0,1)
        b = board(6,[allPents[x] for x in a[6:] ])
        b.dancinglinks(0,1)


#Executions time: 0.05 seconds
def testAll3(allPents):
    b = board(3,allPents)
    b.dancinglinks(0,1)

#Executions time: 0.29 seconds
def testAll3iter(allPents):
    allThree = list(itertools.combinations(allPents,3))
    for a in range(len(allThree)):
        b = board(3,list(allThree[a])[:])
        b.dancinglinks(0,1)

#BOARD_SIZE = 3 | Executions time: 0.03 seconds
#BOARD_SIZE = 4 | Executions time: 0.25 seconds
#BOARD_SIZE = 5 | Executions time: 1.98 seconds
#BOARD_SIZE = 6 | Executions time: 12.81 seconds
#BOARD_SIZE = 7 | Executions time: 95.08 seconds
def testAll(allPents,BOARD_SIZE):
    b = board(BOARD_SIZE,allPents)
    b.dancinglinks(0,1)

def testAllDups(allPents,BOARD_SIZE):
    b = board(BOARD_SIZE,allPents)
    b.dancinglinks(1,1)

#Executions time: 126.77 seconds
def SMALL_SLAM_A(allPents):
    b = board(8,[allPents[4],allPents[5],allPents[11],allPents[1],allPents[3],allPents[9],allPents[8],allPents[0]])
    b.dancinglinks(0,1)


def tilingPlane(allPents,BOARD_SIZE):
    b = board(BOARD_SIZE,allPents)
    b.dancinglinks(2,1)



#################
#Bin Solver Test#
#################

###TEST WITH 1
#@param pentaContainer
def testBinOne(penta):
#    print(penta)
    one = board(1,[penta])
    print(one)
    one.binSolver(1)

####TEST WITH 3
def testBinThree(allPents,pentas):
    b = board(3,[allPents[x] for x in pentas])
    b.binSolver(1)

####TEST WITH ALL
#BOARD_SIZE = 3 | Executions time: 0.15 seconds
#BOARD_SIZE = 4 | Executions time: 33.91 seconds
def testBinAll(allPents,BOARD_SIZE,pentas):
    b = board(BOARD_SIZE,[allPents[x] for x in pentas])
    b.binSolver(1)

def testBinIters(allPents,BOARD_SIZE):
    allThree = list(itertools.combinations(allPents,BOARD_SIZE))
    for a in range(len(allThree)):
        b = board(BOARD_SIZE,list(allThree[a])[:])
        b.binSolver(1)

