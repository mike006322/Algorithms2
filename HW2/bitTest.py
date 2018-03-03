a = '10010'
b = '11111'

def diff(x, y):
    #input strings of 1's and 0's and output string where "1" means they differ
    return int(x, 2) ^ int(y, 2)


def bitCount(int_type):
    int_type
    count = 0
    while (int_type):
        count += (int_type & 1)
        int_type >>= 1
    return count

def d(x, y):
    return bitCount(diff(x,y))
    

print(d(a, b))