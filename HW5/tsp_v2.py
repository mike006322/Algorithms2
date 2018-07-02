"""
Traveling Salesman Problem
Pseudocode in tsp_pseudocode.txt
Version 3: use binary numbers to represent subsets instead of sets
"""

from math import sqrt
from numpy import inf
import time


def find_subsets(n):
    """
    Computes subsets of {1, ..., n} organized by cardinality.
    Subsets represented by binary numbers of length n, where '1' means included and '0' means not included
    Outputs is a dictionary with keys being cardinality and values being subset representations.
    """

    subsets = dict()
    for cardinality in range(n + 1):
        subsets[cardinality] = []
    for subset in range(2**n):
        subsets[bin(subset).count('1')].append(subset)
    return subsets


def make_set(n):
    """
    Converts binary representation of subset to actual set.
    """
    bin_string = bin(n)[2:]
    subset = set()
    for i in range(len(bin_string)):
        if bin_string[-(i+1)] == '1':
            subset.add(i)
    return subset

def make_set_representation(input_set):
    """
    Converts a set of numbers to sum of 2**number
    """
    sum = 0
    for num in input_set:
        sum += 2**num
    return sum


def dist(x, y):
    return sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)


def create_distance_cache(points):
    cache = dict()
    for c in points:
        cache[c] = dict([(d, dist(c, d)) for d in points])
    return cache


class ProgressChecker:
    def __init__(self, total):
        self.total = total
        self.start_time = time.time()

    def report(self, current_number):
        if current_number == 0:
           if self.total > 14:
               print('Creating subsets...')
        time_check = time.time()
        if time_check - self.start_time > 2:
            print('Done calculating subsets size {} out of {}'.format(current_number, self.total))

    def time_elapsed(self):
        now = time.time()
        elapsed_time = now - self.start_time
        return elapsed_time


def traveling_salesman(points):
    """
    Returns length of shortest cycle through every point
    """

    n = len(points)
    progress = ProgressChecker(n)
    print(n, ' points')
    N = [x for x in range(n)]
    # 2D array is implemented as a dicationary of dictionaries, A;
    # A has keys = subsets that include first point, values = dictionaries of calculated distances;
    # those dictionaries have keys = destinations, values = calculated distance;
    # for example, A[{0,1,2}][2] is the calculated distance to point 2 for the subset {0,1,2}
    A = dict()
    progress.report(0)
    subsets_without_first_element = find_subsets(n-1)
    # Base case:
    # A[S][1] = {0 if S = {1}, inf otherwise}. Wait until the subsets are created to initialize them
    A[1] = {0: 0}

    cached_distance = create_distance_cache(points)

    # Fill in the '2D array' by first iterating over the subsets by subset size and then iterate over the destinations, j, in each subset
    for m in range(2, n + 1):
        # create list of subsets of size m - 1 that don't have 1, called subsets_size_m to represent subsets of size m that have the first point, N[0] = 0

        for subset in subsets_without_first_element[m - 1]:
            subset = subset*2+1
            A[subset] = {0: inf}
            subset_set = make_set(subset)
            for j in subset_set:
                if j != 0:
                    possible_mins = []
                    for k in subset_set:
                        if k != j:
                            possible_mins.append(A[subset - 2**j][k] + cached_distance[points[k]][points[j]])
                    A[subset][j] = min(possible_mins)

        progress.report(m)
    shortest_paths = A[int('1'*n, 2)]
    for destination in shortest_paths:
        dist_to_start = cached_distance[points[0]][points[destination]]
        shortest_paths[destination] = shortest_paths[destination] + dist_to_start
    final_destination = min(shortest_paths, key=shortest_paths.get)
    shortest_path_length = shortest_paths[final_destination]

    # recreate the route:
    route = []
    traversed_points = set(N)
    destination = final_destination
    traversed = shortest_path_length
    while traversed_points:
        route.append(destination)
        traversed_points = traversed_points - {destination}
        if len(traversed_points) == 0:
            break
        previous_destination = destination
        destination = next(point for point, distance in A[make_set_representation(traversed_points)].items() if (distance - (traversed - dist(points[point], points[destination]))) < .000000001)
        traversed = traversed - dist(points[destination], points[previous_destination])
    route.reverse()
    return 'Shortest cycle length is: {} \nRoute indexes: {} \nRunning time: {} \n'.format(shortest_path_length, route, progress.time_elapsed())


def get_points(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        points = []
        number_of_points = int(lines[0])
        for line in lines[1:number_of_points + 1]:
            points.append(tuple(map(float, line.split())))
        return points


def test1():
    points = get_points('test1.txt')
    print(traveling_salesman(points))
    # straight line


def test2():
    points = get_points('test2.txt')
    print(traveling_salesman(points))
    # 'C' shape


def test3():
    points = get_points('test3.txt')
    print(traveling_salesman(points))
    # triangle


def test4():
    points = get_points('test4.txt')
    print(traveling_salesman(points))
    # first 17 points of tsp.txt


def main():
    points = get_points('tsp.txt')
    print(traveling_salesman(points))


if __name__ == '__main__':
    #main()
    test1()
    test2()
    test3()
    test4()
