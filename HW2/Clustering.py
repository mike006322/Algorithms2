#Clustering greedy algorithm
#given edge lengths (distances between each point)
#each point starts off in the own cluster, 
#i.e. list of length n where the entries are the cluster leads, initialized to a[i] = i
#take closest pair of points not in the same cluster and fuse them
#output maximum spacing of a 4-clustering
#spacing is min(d,p) where d, p are separated points
#idea: 1. sort edge list 2. travese edge list checking if points are separated and merge if they are
#3. do that until there are only 4 clusters left and then check the next separated

edges = []
for line in open('clustering1.txt', 'r'):
    entries = tuple(map(int,line.split()))
    edges.append(entries)
n = edges[0][0] #500
edges = edges[1:]

nodes = []
for i in range(501):
    nodes.append((i,0))
    
def find(x, array):
    #find the leader of the cluster and compresses the path along the way
    d = x
    path = []
    while d != array[d][0]:
        path.append(d)
        d = array[d][0]
    #path compression
    for j in path:
        array[j] = (d, array[j][1])
    return d
    
    #change areSep below to use find function

def areSep(x, y, array):
    #returns boolean True if separated, False if in same cluster
    d = find(x, array)
    p = find(y, array)
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
        
edges.sort(key = lambda x: x[2])
       
test = [(0,0),(1,0),(2,0),(3,0),(4,0)]

numUnions = 0
i = 0
while numUnions < 496:
    edge = edges[i]
    x = edge[0]
    y = edge[1]
    if areSep(x, y, nodes):
        numUnions += 1
        union(x, y, nodes)
    i += 1

answer = False
while answer == False:
    edge = edges[i]
    x = edge[0]
    y = edge[1]
    dis = edge[2]
    if areSep(x, y, nodes):
        answer = True
    i += 1
print(edge)
print(edges[i+1])
print(areSep(414,455, nodes))

#print(edges[0])
#print(areSep(1,2,test))
#print(find(1, test))
#print(test)

        