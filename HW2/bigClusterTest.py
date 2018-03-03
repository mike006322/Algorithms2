#Must come up with an implemenation that can quickly compute minimum Hamming distances
#Clustering greedy algorithm for large file
import time

points = set()
for line in open('clustering_big.txt', 'r'):
    points.add(line.replace(" ", "").strip())
    
first = open('clustering_big.txt', 'r').readline().replace(" ", "").strip()
points.remove(first)

#len(points) = 198788
#The length of each p in points is 24

def hDisOne(bit_string):
    #returns set of strings *exactly* Hamming distance one away
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

def hDisTwo(bit_string):
    #returns set of strings with Hamming distance 1 or 2
    res = set()
    one = hDisOne(bit_string)
    for i in one:
        two = hDisOne(i)
        for j in two:
            res.add(j)
    res = res.union(one)
    res.remove(bit_string)
    return res

def find(x, dic):
    #find the leader of the cluster and compresses the path along the way
    d = x
    path = []
    while d != dic[d][0]:
        path.append(d)
        d = dic[d][0]
    #path compression
    for j in path:
        dic[j] = (d, dic[j][1])
    return d

def areSep(x, y, dic):
    #returns boolean True if separated, False if in same cluster
    d = find(x, dic)
    p = find(y, dic)
    if d != p:
        return True
    else:
        return False
        
def union(x, y, array):
    d = find(x, array)
    p = find(y, array)
    if array[d][1] == array[p][1]:
        array[d] = (p, array[d][1])
        array[p] = (array[p][0], array[p][1] + 1)
    if array[d][1] <= array[p][1]:
        array[d] = (p, array[d][1])
    else:
        array[p] = (d, array[p][1])



k = len(points) # already clustered points with distance 0 by removing identicle points with set datastructure
listP = list(points)

uf = dict()
for i in range(198788):
    uf[listP[i]] = (listP[i],0)

start = time.time()
#for i in range(10000):
for i in range(len(listP)):
    point = listP[i]
    two = hDisTwo(point)
    for j in two:
        if j in points:
            if areSep(j, point, uf):
                k -= 1
                union(j, point, uf)
end = time.time()
duration = end - start

print(k)
print(duration)