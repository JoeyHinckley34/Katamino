#HELPER FUNCTIONS


#@param x : Number in base ten
#@returns : x in binary
def dec_to_bin(x):
    return int(bin(x)[2:])

#@param x : Number to be converted to binary
#@param z : Number of leading zeros
#@returns : x in binary with z leaing zeros
def dec_to_bin_zeros(x,z):
    return f'{int(bin(x)[2:]):0{z}}'
