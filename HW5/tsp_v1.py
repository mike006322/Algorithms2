# Traveling Salesman Problem
# Pseudocode in tsp_pseudocode.txt

from math import sqrt
from numpy import inf
from itertools import chain, combinations
import time


def subsets_with_first_element(lst):
    # input is a list
    # output: set of frozensets of all possible combinations of elements from input (**must include first element**)
    # size of output is 2**(n-1)
    xs = list(lst[1:])
    res = list(chain.from_iterable(combinations(xs, n) for n in range(1, len(xs) + 1)))
    for i in range(len(res)):
        res[i] = frozenset(lst[0:1] + list(res[i]))
    res = set(res)
    return res


def find_subsets_of_size(input_set, size):
    return set(combinations(input_set, size))


def dist(x, y):
    return sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)


def create_distance_cache(data):
    cache = dict()
    for c in data:
        cache[c] = dict([(d, dist(c, d)) for d in data])
    return cache


class ProgressChecker:
    def __init__(self, data_size):
        self.data_size = data_size
        self.start_time = time.time()
    def report(self, number):
       if number == 0:
           if self.data_size > 14:
               print('Creating subsets...')
       else:
           self.time_check = time.time()
           if self.time_check - self.start_time > 2:
               print('Done calculating subsets size {} out of {}'.format(number, self.data_size))
    def time_elapsed(self):
        now = time.time()
        elapsed_time = now - self.start_time
        return elapsed_time


def traveling_salesman(data):
    # returns length of shortest cycle through every point
    n = len(data)
    progress = ProgressChecker(n)
    print(n, ' points')
    N = [x for x in range(n)]
    # 2D array is implemented as a dicationary of dictionaries, A;
    # A has keys = subsets that include first point, values = dictionaries of calculated distances;
    # those dictionaries have keys = destinations, values = calculated distance;
    # for example, A[{0,1,2}][2] is the calculated distance to point 2 for the subset {0,1,2}
    A = dict()

    # Base case:
    # A[S][1] = {0 if S = {1}, inf otherwise}. Wait until the subsets are created to initialize them
    progress.report(0)
    #for subset in subsets_with_first_element(N):
    #    A[subset] = {0: inf}
    A[frozenset({0})] = {0: 0}

    cached_distance = create_distance_cache(data)

    # Fill in the '2D array' by first iterating over the subsets by subset size and then iterate over the destinations, j, in each subset
    for m in range(2, n + 1):
        # create list of subsets of size m - 1 that don't have 1, called subsets_size_m to represent subsets of size m that have the first point, N[0] = 0
        subsets_size_m = find_subsets_of_size(N[1:], m - 1)
        for subset in subsets_size_m:
            subset = frozenset(subset).union({0})
            A[subset] = {0: inf} # This normally would have been done during the base case

            for j in subset:
                if j != 0:
                    possible_mins = []
                    for k in subset:
                        if k != j:
                            possible_mins.append(A[subset - {j}][k] + cached_distance[data[k]][data[j]])
                    A[subset][j] = min(possible_mins)
        progress.report(m)
    shortest_paths = A[frozenset(N)]
    for destination in shortest_paths:
        dist_to_start = cached_distance[data[0]][data[destination]]
        shortest_paths[destination] = shortest_paths[destination] + dist_to_start
    final_destination = min(shortest_paths, key=shortest_paths.get)
    shortest_path_length = shortest_paths[final_destination]

    # recreate the route:
    route = []
    points = set(N[:])
    destination = final_destination
    traversed = shortest_path_length
    while points:
        route.append(destination)
        points = points - {destination}
        if len(points) == 0:
            break
        previous_destination = destination
        try:
            destination = next(point for point, distance in A[frozenset(points)].items() if distance == (traversed - dist(data[point], data[destination])))
        except StopIteration:
            # this exception occurs if there is no equal distance due to rounding error
            destination = next(point for point, distance in A[frozenset(points)].items() if (distance - (traversed - dist(data[point], data[destination]))) < .001)
        traversed = traversed - dist(data[destination], data[previous_destination])
    route.reverse()

    return 'Shortest cycle length is: {} \nRoute indexes: {} \nRunning time: {} \n'.format(shortest_path_length, route, progress.time_elapsed())


def test1():
    import tsp_tests
    print(traveling_salesman(tsp_tests.test1))


def test2():
    import tsp_tests
    print(traveling_salesman(tsp_tests.test2))


def test3():
    import tsp_tests
    print(traveling_salesman(tsp_tests.test3))


def test4():
    import tsp_tests
    print(traveling_salesman(tsp_tests.test4))


def main():
    data = [
        (20833.3333, 17100.0000),
        (20900.0000, 17066.6667),
        (21300.0000, 13016.6667),
        (21600.0000, 14150.0000),
        (21600.0000, 14966.6667),
        (21600.0000, 16500.0000),
        (22183.3333, 13133.3333),
        (22583.3333, 14300.0000),
        (22683.3333, 12716.6667),
        (23616.6667, 15866.6667),
        (23700.0000, 15933.3333),
        (23883.3333, 14533.3333),
        (24166.6667, 13250.0000),
        (25149.1667, 12365.8333),
        (26133.3333, 14500.0000),
        (26150.0000, 10550.0000),
        (26283.3333, 12766.6667),
        (26433.3333, 13433.3333),
        (26550.0000, 13850.0000),
        #(26733.3333, 11683.3333),
        #(27026.1111, 13051.9444),
        #(27096.1111, 13415.8333),
        #(27153.6111, 13203.3333),
        #(27166.6667, 9833.3333),
        #(27233.3333, 10450.0000)
    ]
    print(traveling_salesman(data))

if __name__ == '__main__':
    main()
    #test1()
    #test2()
    #test3()
    #test4()
