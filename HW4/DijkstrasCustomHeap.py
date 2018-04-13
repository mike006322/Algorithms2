def Dijkstras(a, n, s):
    from HeapDelete import Heap
    from numpy import inf
    #input is (a, num verticies, vertex taking shortest path from)
    # a is graph of the form {node1: {node2: distance, node3: distance, ... }, ...}
    #n = number of verticies
    #s = number of vertex to compute shortest paths from
    #output of Dijkstras is a n-length list of shortest paths from vertex
    
    X = {s} # Verticies passed so far
    A = {s:0} # Computed shortest path distances
    V = set(range(1, n+1))
    min_heap = Heap() # stores nodes in form node = (key, label)
    #for each vertex connected to s add '(distance, node)'
    #for all other vertex add '(inf, node)'
    if s in a:
        min_heap.heapify([(inf, x) for x in V - X - set(a[s].keys())])
        for v in a[s]:
            min_heap.insert((a[s][v], v))
    else:
        min_heap.heapify([(inf, x) for x in V - X])
    
    while X != V:
        # find minimum A[v] + len(v,w) among edges (v,w) for all v in X and w not in X
        # call it (vStar, wStar)
        m = min_heap.extractMin() # gives us (distance, node) # instead of (node, distance) 
        X.add(m[1])
        A[m[1]] = m[0]
        #for each edge (v, m[1]) out of m[1], a[m[1]][v] = distance to v
        if m[1] in a:
            for v in a[m[1]]: 
                if v in V - X:
                    min_heap.heapList[0] = (0,0)
                    vKey = min_heap.heapList[min_heap.heapIndexDict[v]][0]
                    min_heap.delete((vKey,v))
                    vKey = min(vKey, A[m[1]] + a[m[1]][v])
                    min_heap.insert((vKey,v))
    return A
    
if __name__ == '__main__':
    a ={}
    for line in open('dijkstraData.txt', 'r'):
        b = list(line.split())
        a[int(b[0])] = {}
        for i in b[1:]: #'node, distance'
            node, distance = i.split(',')
            a[int(b[0])][int(node)] = int(distance)
    n = 200
    m = 1
    import time
    start = time.time()
    P = Dijkstras(a, n, m)
    stop = time.time()
    total = stop - start
    print('time to run: ', total)
    # P is shortest path distances from 1 
    print(P[7]) #2599
    print(P[37]) #2610
    print(P)
    print(min(P.items(), key = lambda x: x[1])[1])
