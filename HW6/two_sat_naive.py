"""
Naive implementation of 2sat problem
This passes all tests but much to slow for the data we want to use it on
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
    """randomly assigns True and False values to n variables"""
    assignment = []
    i = 0
    while i < n:
        assignment.append(bool(random.getrandbits(1)))
        i += 1
    return assignment

def check_assignment(assignment, conditions):
    """checks if the assignment of variables satisfies the conditions
    returns list of indexes of all assignments not satisfied"""
    conditions_not_satisfied = []
    for i in range(len(conditions)):
        #conditions[i] = (number, number), negative if false
        condition = conditions[i]
        a = condition[0]
        b = condition[1]
        satisfied = False
        if assignment[abs(a) - 1] == True and a > 0:
            satisfied = True
        if assignment[abs(a) - 1] == False and a < 0:
            satisfied = True
        if assignment[abs(b) - 1] == True and b > 0:
            satisfied = True
        if assignment[abs(b) - 1] == False and b < 0:
            satisfied = True
        if satisfied == False:
            return [i] # this line makes it run much faster (n times)
            conditions_not_satisfied.append(i)
    return conditions_not_satisfied

def modify_assignment(assignment, conditions, conditions_not_satisfied):
    """returns assignment with a change in one variable in order to satisfy one random condition it didn't previously"""
    condition = conditions[random.choice(conditions_not_satisfied)]
    a = condition[0]
    b = condition[1]
    # find whether it's a or b not satisfied
    not_satisfied = None
    if assignment[abs(a) - 1] != True and a > 0:
        not_satisfied = a
    if assignment[abs(a) - 1] != False and a < 0:
        not_satisfied = a
    if assignment[abs(b) - 1] != True and b > 0:
        not_satisfied = b
    if assignment[abs(b) - 1] != False and b < 0:
        not_satisfied = b
    if assignment[abs(not_satisfied) - 1] == True:
        assignment[abs(not_satisfied) - 1] = False
    else:
        assignment[abs(not_satisfied) - 1] = True


def two_sat(conditions):
    print('starting two_sat...')
    n = len(conditions)
    i = 0
    while i <= math.log2(n):
        print('i = ', i)
        assignment = initial_assignment(n)
        j = 0
        while j <= 2*n**2:
            conditions_not_satisfied = check_assignment(assignment, conditions)
            if len(conditions_not_satisfied) == 0:
                return True
            else:
                modify_assignment(assignment, conditions, conditions_not_satisfied)
            j += 1
            if j%10 == 0:
                print('j = ', j)
        i += 1
    return False

if __name__ == '__main__':
    conditions = get_conditions("2sat1.txt")
    print(len(conditions))
    print(two_sat(conditions))
