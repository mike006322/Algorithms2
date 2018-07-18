"""
Kosaraju's two-pass algorithm for computing strongly connected components
First run Depth First Search on graph with edges reversed
Then run Depth First Search on the original graph
"""

import sys
import collections

def reorder_graph(G, ordering):
    """
    returns G but with every node renamed according to ordering
    """
    orderedGraph = dict()
    for i in G:
        orderedGraph[ordering[i]] = [ordering[j] for j in G[i]]
    return orderedGraph

def reverse_ordering(reorderedg, ordering):
    """
    undoes the naming applied by 'reorder_graph'
    """
    reverse_ordering = {v: k for k, v in ordering.items()}
    graph = dict()
    for i in reorderedg:
        graph[reverse_ordering[i]] = [reverse_ordering[j] for j in reorderedg[i]]
    return graph


def kosaraju(g, n):
    ordering = collections.defaultdict(int)

    def DFS(Graph, n):
        """
        input is dictionary of adjacency lists and number of nodes
        nodes are labeled from 1 to n
        output is dictionary of connected components while also modifying global 'ordering'
        """
        connected_components = dict()
        time = 1
        nonlocal ordering
        visited = set()
        for i in range(n,0,-1):
            if i in visited:
                continue
            visited.add(i)
            start = i
            if i % 1000 == 0:
                print('currently on {}'.format(i))
            stack = collections.deque()
            stack.append(start)
            component = set()
            while stack:
                v = stack.popleft()
                if v not in component:
                    component.add(v)
                    stack.appendleft(v)
                    if v in Graph:
                        for w in Graph[v]:
                            if w not in component and w not in visited:
                                visited.add(w)
                                stack.appendleft(w)
                else:
                    if v not in ordering:
                        ordering[v] = time
                        time += 1
            connected_components[i] = component
        return connected_components

    print('Making reverse graph...')
    reverse_graph = collections.defaultdict(set)
    for x in g:
        for y in g[x]:
            reverse_graph[y].add(x)

    DFS(reverse_graph, n) # gets ordering
    Reverse = {} # clears aReverse from memory
    reorderedg = reorder_graph(g, ordering)
    SCCs = DFS(reorderedg, n)

    reverse_ordering = {v: k for k, v in ordering.items()}
    original_named_SCCs = dict()
    for component in SCCs:
        original_named_SCCs[reverse_ordering[component]] = {reverse_ordering[j] for j in SCCs[component]}

    return original_named_SCCs

if __name__ == '__main__':
    sys.getrecursionlimit()
    n = 875714 # number of nodes in graph
    a = collections.defaultdict(set)
    for line in open('SCC.txt', 'r'):
        b = list(map(int, line.split())) # list begining with vertex followed by adjacent verticies
        a[b[0]].add(b[1])
    segment = kosaraju(a, n)
    print(sorted([len(segment[i]) for i in segment]))
