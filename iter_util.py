import itertools
 
def cartesian_product(arr1, arr2):
 
    # return the list of all the computed tuple
    # using the product() method
    return list(itertools.product(arr1, arr2))
   
# Driver Function
if __name__ == "__main__":
    size = 3
    length = 2

    x_cords = [i for i in range(size)]
    y_cords = [i for i in range(length)]

    all_cords = cartesian_product(x_cords, y_cords)
    
    Penta_Cords = all_cords
    
    for i in range(size-1):
        Penta_Cords = cartesian_product(Penta_Cords,all_cords)

    for p in range(len(Penta_Cords)):
        print(p)
        
        
#    print(type(Penta_Cords))
