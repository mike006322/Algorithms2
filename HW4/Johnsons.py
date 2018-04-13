def Johnsons(edges, n, m):
#-----------------------------------------------
#Johnson's algorithm: 
#Finds all-pairs shortest path distances
#Create new graph with new node, s, with edges to all other nodes length 0
#Run Bellman Ford and compute shortest paths from s to all other nodes
#assign each vertex, v, a weight, Pv, that is it's shortest path from s
#Create new set of edges: for c(u,v) in G, c'(u,v) = c + Pu - Pv
#run Dijkstra's algorithm for each vertex in G to every other vertex with edge lengths c'
#unweight the distances, i.e. each d(u,v) = d'(u,v) - Pu + Pv
#------------------------------------------------
    from BellmanFord import BellmanFord
    from DijkstrasCustomHeap import Dijkstras
    
    #Create new graph with new node, s, with edges to all other nodes length 0
    edges_with_s = edges[:]
    for i in range(1, n+1):
        edges_with_s.append([n+1, i, 0])
    #Run Bellman Ford and compute shortest paths from s to all other nodes
    shortest_paths_from_s = BellmanFord(edges_with_s, n+1, n+1) 
        #(edges, num verticies, vertex taking shortest path from)
    #output of BellmanFord is list of distances from s (zero indexed)
    #assign each vertex, v, a weight, Pv, that is it's shortest path from s
    weights = dict()
    for i in range(1, n+1):
        weights[i] = shortest_paths_from_s[i]
    #Create new set of edges: for c(u,v) in G, c'(u,v) = c + Pu - Pv
    weighted_edges = edges[:]
    for i in range(len(weighted_edges)):
        weighted_edges[i] = weighted_edges[i][0:2] + [weighted_edges[i][2] + weights[weighted_edges[i][0]] - weights[weighted_edges[i][1]]]
    #run Dijkstra's algorithm for each vertex in G to every other vertex with edge lengths c'
    #transform weighted_edges into graph for Dijkstra
    a = {}
    for edge in weighted_edges:
        if edge[0] in a:
            a[edge[0]][edge[1]] = edge[2]
        else:
            a[edge[0]] = {}
            a[edge[0]][edge[1]] = edge[2]
    # a is graph of the form {node1: {node2: distance, node3: distance, ... }, ...}
    res = [[0]] + [[]]*(n) #index goes from 0 to n
    mins = []
    for i in range(1, n+1):
        res[i] = Dijkstras(a, n, i)
            #(graph, num verticies, vertex taking shortest path from)
        if i%10 == 0:
            print("Dijkstra complete for ", i)
        #output of Dijkstras is a n-length list of shortest paths from vertex i
    #unweight the distances, i.e. each d(u,v) = d'(u,v) - Pu + Pv
    for i in range(1, n+1):
        for j in range(1, n+1):
            res[i][j] = res[i][j] - weights[i] + weights[j]
    return res

if __name__ == '__main__':
    edges = []
    for line in open('g3.txt', 'r'):
        add = list(map(int, line.split()))
        if len(add) > 2:
            edges.append(add)
    #n = edges[0][0] #number of verticies
    n = 1000
    #m = edges[0][1] #number of edges
    m = len(edges)
    #edges = edges[1:]
    #'edges' is a list of lists of form [tail, head, length]
    import time
    start = time.time()
    s = Johnsons(edges, n, m)
    stop = time.time()
    total = stop - start
    print('time to run: ', total)
    m = 0 
    for i in range(1, n+1):
        if min(s[i].items(), key = lambda x: x[1])[1] < m:
            m = min(s[i].items(), key = lambda x: x[1])[1]
    print(m)
                        
# g1.txt has a negative cycle
# g2.txt has a negative cycle
