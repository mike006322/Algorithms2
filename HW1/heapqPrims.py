from numpy import inf
from graphHeap import MikesGraphHeap
import heapq

edges = []
for line in open('edges.txt', 'r'):
    edges.append(tuple(map(int,line.split())))
nnodes = edges[0][0] #number of nodes, 500 in edges.txt
nedges = edges[0][1] #number of edges
del edges[0]
#graph has elements listed as edges (vertex 1, vertex 2, cost of edge)

a = {}
for i in range(1, nnodes+1):
    a[i] = {}
for edge in edges:
    a[edge[0]][edge[1]] = edge[2]
    a[edge[1]][edge[0]] = edge[2]
# a is graph of the form {node1: {node2: distance, node3: distance, ... }, ...}


TotalCost = 0
V = set(range(1,nnodes+1))
X = set() #set of verticies spanned so far
T = [] #verticies spanned by tree so far
initial = 1
X.add(initial) #seed

heapFill = V - X - set(a[initial].keys()) #all of the nodes that 1 doesnt have an edge to, to have key of inf in M
M = [(inf, x) for x in heapFill]
heapq.heapify(M)
for node in a[initial]: 
    heapq.heappush(M, (a[initial][node], node))

while X != V: 
    #choose e = (u,v), cheapest edge with u in X and v in V - X
    m = heapq.heappop(M) # gives us (v, vkey) where the key is the lowest edge value
    X.add(m[1]) # from m = min(node, value)
    TotalCost += m[0]
    for v in a[m[1]]:
        if v in V - X:
            for j in M:
                if j[1] == v:
                    vKey = j[0]
                    M.remove(j)
                    break
            vKey = min(vKey, a[m[1]][v])
            heapq.heappush(M, (vKey, v))
            heapq.heapify(M)

print(TotalCost)
