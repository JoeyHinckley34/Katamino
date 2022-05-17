import itertools

#@param a : a list
#@param size : the desired size of the lists
#@returns a list of all possible lists with the length of the given size by added zeros to the front or the end of list a
def addzeros(a,size):
    lists = []
    lists = add1(a,size,lists)
    return [list(b) for b in list(set(tuple(i) for i in lists)) ]

def add1(a,size,b):
    if len(a) > size:
        b.append(a)
        return b
        
    elif len(a) == size:
        b.append(a)
        return b
        
    else:
        a1 = a.copy()
        a1.insert(0,0)
#        b.append(a1)
        
        a2 = a.copy()
        a2.append(0)
#        b.append(a2)
        add1(a1,size,b)
        add1(a2,size,b)
        return b


#@param a : a list of integers
#@param N : board size
#@returns list of lists created by multiplying every value of the list by two until we hit the max
def multiplyList(a,N):
    lists = [a.copy()]
    lists = multiply1(a,N,lists)
    return [list(b) for b in list(set(tuple(i) for i in lists)) ]
    
def multiply1(a,N,lists):
#    print(type(max(a)),a)
    if max(a) > (2**(N-1)-1):
        return lists
    
    else:
        a1 = [i*2 for i in a]
        lists.append(a1)
        multiply1(a1,N,lists)
        return lists
  
  
def checker(list,N):
    for a in list:
        if a != N:
            return False
#    print(list)
    return True
            
def test():
    A = [2,2,7]
    B = [3,2,2,2]
    C = [1,3,1,1]

    all = [A,B,C]


    mult = []
    for a in all:
        print(f'{multiplyList(a,3)}')
        mult.append(multiplyList(a,3))
        
    print(f'mult {mult}')
    allmult = []
    
    
    
    for element in itertools.product(*mult):
        allmult.append(list(element))
        
    print(f'allmult {allmult}')

    zeros = []
    for a in allmult:
        print(f'a : {a}')
        z = []
        for b in a:
            z.append( addzeros(b,5) )
        zeros.append(z[:])

    for x in zeros:
        print(f'z: {x}')
    #
    allSums = []

    for a in zeros:
#        print(a)
        for element in itertools.product(*a):
            print (element)
            sums = [0 for i in range(5)]
            for penta in element:
                for i in range(len(penta)):
                    sums[i] += penta[i]
                    
                    
            if checker(sums,7):
                print(element)
                print(sums)
                allSums.append(element)
                
                
                
    for a in allSums:
        for b in range(len(a)):
            print(a[b])


def main():
    test()

if __name__ == '__main__':
    main()





