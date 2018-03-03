#given a string of 0's and 1's, output a list of strings that have hamming distance 1 away
def hDisOne(bit_string):
    res = set()
    for i in range(len(bit_string)):
        if bit_string[i] == '1':
            if i < len(bit_string) - 1:
                changed = bit_string[:i] + '0' + bit_string[i+1:]
            else:
                changed = bit_string[:i] + '0'
        else:
            if i < len(bit_string) - 1:
                changed = bit_string[:i] + '1' + bit_string[i+1:]
            else:
                changed = bit_string[:i] + '1'
        res.add(changed)
    return res

#Now hamming distance of 2 (within 2)
#Find set of distance 1, then take distance of one from those

def hDisTwo(bit_string):
    res = set()
    one = hDisOne(bit_string)
    for i in one:
        two = hDisOne(i)
        for j in two:
            res.add(j)
    res = res.union(one)
    return res

print(hDisOne('000'))
print(hDisTwo('0000'))