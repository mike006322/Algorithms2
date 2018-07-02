def BellmanFord(edges, n, s):
    """
    input is (edges, num verticies, vertex taking shortest path from)
    'edges' is a list of lists of form [tail, head, length]
    n = number of verticies
    s = number of vertex to compute shortest paths from
    output of BellmanFord is list of distances from s
    """
    
    from numpy import inf
    
    # first take edges and turn it into the graph of the following form:
    a = {}
    for edge in edges:
        if edge[1] in a:
            a[edge[1]][edge[0]] = edge[2]
        else:
            a[edge[1]] = {}
            a[edge[1]][edge[0]] = edge[2]
    # a is graph of the form {node1: {node2: distance, node3: distance, ... }, ...} WHERE node1 IS THE HEAD
    
    # have current array, A, and a previous subproblem array, B
    A = [inf]*(n+1)
    A[s] = 0
    B = A[:]
    
    i = 1
    while i < n:
        for v in range(1, n+1):
            edges_to_v = {}
            if v in a:
                edges_to_v = a[v] # dictionary of edges to v in form {node1: distance, node2, distance}
            if edges_to_v == {}:
                minCost = inf
            else:
                minCost = min({B[e] + edges_to_v[e] for e in edges_to_v})
            A[v] = min(B[v], minCost)
        B = A[:]
        i += 1
    return A

if __name__ == '__main__':
    edges = []
    for line in open('dijkstraData.txt', 'r'):
        b = list(line.split())
        for i in b[1:]: #'head, length'
            head, length = i.split(',')
            tail = b[0]
            edges.append([int(tail), int(head), int(length)])
    # 'edges' is a list of lists of form [tail, head, length]
    # graph is list of directed edges in form [tail, head, length]
    n = 200
    m = 1
    import time
    start = time.time()
    P = BellmanFord(edges, n, m)
    stop = time.time()
    total = stop - start
    print('time to run: ', total)
    # P is shortest path distances from 1 
    print(P[7]) #2599
    print(P[37]) #2610
    print(P[1])
    print(P)