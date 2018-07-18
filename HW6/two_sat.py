import collections
import modular_kosaraju as kosaraju

def make_graph(file_path):
    """
    returns tuple:
    n - first line of file, number of variables and conditions
    graph - implication graph made from the conditions
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
        graph = collections.defaultdict(set)
        n = int(lines[0])
        for c in lines[1: n + 1]:
            a, b = tuple(map(int, c.split()))
            if a > 0 and b > 0:
                graph[n + a].add(b)
                graph[n + b].add(a)
            if a > 0 and b < 0:
                graph[n + a].add(n + abs(b))
                graph[abs(b)].add(a)
            if a < 0 and b > 0:
                graph[abs(a)].add(b)
                graph[n + b].add(n + abs(a))
            if a < 0 and b < 0:
                graph[abs(a)].add(n + abs(b))
                graph[abs(b)].add(n + abs(a))
        return n, graph

def two_sat(file_path):

    n, implication_graph = make_graph(file_path)
    SCCs = kosaraju.kosaraju(implication_graph, 2*n)
    for component in SCCs:
        for var in SCCs[component]:
            if var + n in SCCs[component]:
                return "impossible"
    return "possible"

if __name__ == '__main__':
    print(two_sat('2sat6.txt'))
