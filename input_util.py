from Pentamino_util import Pentamino, PentaContainer

#@param filename : filename we are reading in 'hashedPentas.txt'
#@returns allIters: Array of all pentaminoes
def getPentasFromHash(filename):
    #opens file and reads it line by line
    with open(filename,'r') as myfile:
        data = myfile.read().splitlines()
    #Array of all pentaminoes
    allIters = []
    #loop through all lines in .txt file
    for d in data:
        allIters.append(Pentamino(d))
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
 

 
def getAllPents(DEBUG):
    #Getting Pentaminos from hashes:
    allIters = getPentasFromHash('InputFiles/hashedPentas.txt')
    allDict = generateAllDict(allIters)
    allPents = DictToPentas(allDict)

    # if(DEBUG):
    #     for i in allIters:
    #         #Checking if hashvalues match what is expected
    #         print(f'input hash: {i.h} calculated hash {i.gethash()} \t MATCH {i.h==i.gethash()}\n{i}')

    # if(DEBUG):
    #     print("Dictionary of Pentaminos")
    #     for key,value in sorted(allDict.items()):
    #         print(f'Pentanmino ID: {key} ')
    #         for i in value:
    #             print(i)

    # if(DEBUG):
    #     #print all PentaContainers
    #     for i in allPents:
    #         print(i)
 
    return allPents
