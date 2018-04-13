#Not fast enough because heapq doesn't support deletions at O(logn) time
#See DijkstrasCustomHeap.py which uses a heap with O(logn) delete

def Dijkstras(edges, n, s):
    import heapq
    from numpy import inf
    #input is (edges, num verticies, vertex taking shortest path from)
    #'edges' is a list of lists of form [tail, head, length]
    #n = number of verticies
    #s = number of vertex to compute shortest paths from
    #output of Dijkstras is a n-length list of shortest paths from vertex s
    
    #first take edges and turn it into the graph of the following form:
    a = {}
    for edge in edges:
        if edge[0] in a:
            a[edge[0]][edge[1]] = edge[2]
        else:
            a[edge[0]] = {}
            a[edge[0]][edge[1]] = edge[2]
    # a is graph of the form {node1: {node2: distance, node3: distance, ... }, ...}
    
    X = {s} # Verticies passed so far
    A = {s:0} # Computed shortest path distances
    V = set(range(1, n+1))
    min_heap = [] # stores nodes in form node = (key, label)
    #for each vertex connected to s add '(distance, node)'
    #for all other vertex add '(inf, node)'
    for v in a[s]:
        min_heap.append((a[s][v], v))
    for v in V - X - set(a[s].keys()):
        min_heap.append((inf, v))
    heapq.heapify(min_heap)
    
    while X != V:
        # find minimum A[v] + len(v,w) among edges (v,w) for all v in X and w not in X
        # call it (vStar, wStar)
        m = heapq.heappop(min_heap) # gives us (distance, node) # instead of (node, distance) 
        X.add(m[1])
        A[m[1]] = m[0]
        #for each edge (v, m[1]) out of m[1], a[m[1]][v] = distance to v
        for v in a[m[1]]: 
            if v in V - X:
                vKey = dict((e[1], e[0]) for e in min_heap)[v]
                min_heap.remove((vKey,v)) # min_heap loses heap property
                vKey = min(vKey, A[m[1]] + a[m[1]][v])
                heapq.heapify(min_heap)
                heapq.heappush(min_heap, (vKey,v))
    return A
    
if __name__ == '__main__':
    edges = []
    for line in open('dijkstraData.txt', 'r'):
        b = list(line.split())
        for i in b[1:]: #'head, length'
            head, length = i.split(',')
            tail = b[0]
            edges.append([int(tail), int(head), int(length)])
    #'edges' is a list of lists of form [tail, head, length]
    #graph is list of directed edges in form [tail, head, length]
    n = 200
    m = 1
    import time
    start = time.time()
    P = Dijkstras(edges, n, m)
    stop = time.time()
    total = stop - start
    print('time to run: ', total)
    # P is shortest path distances from 1 
    print(P[7]) #2599
    print(P[37]) #2610
