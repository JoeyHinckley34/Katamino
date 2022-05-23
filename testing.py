import itertools
from main import board

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
    
#Executions time: 0.29 seconds
def testAll3(allPents):
    allThree = list(itertools.combinations(allPents,3))
    for a in range(len(allThree)):
        b = board(3,list(allThree[a])[:])
        b.dancinglinks(0,1)
