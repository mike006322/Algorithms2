"""
Improved to use bitwise operators to test truth
'check_assignment' function returns only 1 index instead of up to n
Much slower than even the naive
"""

import math
import random

def get_conditions(file_path):
    """returns a list of tuples of conditions"""
    with open(file_path, 'r') as f:
        lines = f.readlines()
        conditions = []
        number_of_conditions = int(lines[0])
        for c in lines[1: number_of_conditions + 1]:
            conditions.append(tuple(map(int, c.split())))
        return conditions

def initial_assignment(n):
    """randomly assigns True and False values to n variables
    returns integer with binary representation having 1 in i'th position if i'th variable is True
    index starts at 1"""
    assignment = 0
    i = 1
    while i < n + 1:
        assignment += bool(random.getrandbits(1)) * 2**i
        i += 1
    return assignment

def check_assignment(assignment, conditions):
    """checks if the assignment of variables satisfies the conditions
    returns index of an assignment not satisfied or None if satisfied"""
    for i in range(len(conditions)):
        #conditions[i] = (number, number), negative if false
        condition = conditions[i]
        a = condition[0]
        b = condition[1]
        satisfied = False
        while satisfied == False:
            if assignment & 2**abs(a) != 0 and a > 0:
                satisfied = True
            if assignment & 2**abs(a) == 0 and a < 0:
                satisfied = True
            if assignment & 2**abs(b) != 0 and b > 0:
                satisfied = True
            if assignment & 2**abs(b) == 0 and b < 0:
                satisfied = True
            break
        if satisfied == False:
            return i
    return None

def modify_assignment(assignment, conditions, index):
    """modifies assignment, changing the variable that doesn't satisfy conditions[index]"""
    condition = conditions[index]
    a = condition[0]
    b = condition[1]
    # find whether it's a or b not satisfied
    not_satisfied = None
    while not_satisfied == None:
        if assignment & 2**abs(a) == 0 and a > 0:
            not_satisfied = a
            break
        if assignment & 2**abs(a) != 0 and a < 0:
            not_satisfied = a
            break
        if assignment & 2**abs(a) == 0 and a < 0:
            not_satisfied = b
            break
        if assignment & 2**abs(b) != 0 and b < 0:
            not_satisfied = b
            break
    if assignment & 2**abs(not_satisfied) != 0:
        assignment -= 2**abs(not_satisfied)
    else:
        assignment += 2**abs(not_satisfied)
    return assignment


def two_sat(conditions):
    print('starting two_sat...')
    n = len(conditions)
    i = 0
    while i <= math.log2(n):
        print('i = ', i)
        assignment = initial_assignment(n)
        j = 0
        while j <= 2*n**2:
            condition = check_assignment(assignment, conditions)
            if condition == None:
                return True
            else:
                assignment = modify_assignment(assignment, conditions, condition)
            j += 1
            if j%10 == 0:
                print('j = ', j)
        i += 1
    return False

if __name__ == '__main__':
    conditions = get_conditions("2sat1.txt")
    print(len(conditions))
    print(two_sat(conditions))
