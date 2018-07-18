"""
Naive implementation of 2sat problem
This passes all tests but much to slow for the data we want to use it on
"""

import math
import random
import time

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

saver = 0 # point to resume iterating to help reduce redundancy in check_assignment

def check_assignment(assignment, conditions):
    """checks if the assignment of variables satisfies the conditions
    returns list of indexes of all assignments not satisfied"""
    n = len(conditions)
    for i in range(n):
        #conditions[i] = (number, number), negative if false
        global saver
        condition = conditions[(saver + i)%n]
        a = condition[0]
        b = condition[1]
        satisfied = False
        if assignment[abs(a) - 1] == True and a > 0:
            satisfied = True
        elif assignment[abs(a) - 1] == False and a < 0:
            satisfied = True
        elif assignment[abs(b) - 1] == True and b > 0:
            satisfied = True
        elif assignment[abs(b) - 1] == False and b < 0:
            satisfied = True
        elif satisfied == False:
            res = (saver + i)%n
            saver = (saver + i)%n
            return res
    return None

def modify_assignment(assignment, conditions, index):
    """returns assignment with a change in one variable in order to satisfy one random condition it didn't previously"""
    condition = conditions[index]
    a = condition[0]
    b = condition[1]
    # find whether it's a or b not satisfied
    not_satisfied = None
    if assignment[abs(a) - 1] != True and a > 0:
        not_satisfied = a
    elif assignment[abs(a) - 1] != False and a < 0:
        not_satisfied = a
    elif assignment[abs(b) - 1] != True and b > 0:
        not_satisfied = b
    elif assignment[abs(b) - 1] != False and b < 0:
        not_satisfied = b
    if assignment[abs(not_satisfied) - 1] == True:
        assignment[abs(not_satisfied) - 1] = False
    else:
        assignment[abs(not_satisfied) - 1] = True

class ProgressChecker:
    def __init__(self, n):
        self.total = 2*n**2
        self.start_time = time.time()
        print('starting two_sat...')

    def report(self, current_number, i):
        time_check = time.time()
        if time_check - self.start_time > 2:
            print('j = {}, {}% complete with iteration {}'.format(current_number, current_number//self.total, i))

    def time_elapsed(self):
        now = time.time()
        elapsed_time = now - self.start_time
        return elapsed_time


def two_sat(conditions):
    n = len(conditions)
    progress = ProgressChecker(n)
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
                modify_assignment(assignment, conditions, condition)
            j += 1
            if j%1000000 == 0:
                progress.report(j, i)
                print(progress.time_elapsed())
        i += 1
    return False

if __name__ == '__main__':
    conditions = get_conditions("2sat1.txt")
    print(len(conditions))
    print(two_sat(conditions))
