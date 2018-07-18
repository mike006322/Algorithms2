import unittest
import two_sat

class Test_two_sat(unittest.TestCase):
    '''
    def test_get_conditions(self):
        conditions = two_sat.get_conditions("2sat1.txt")
        self.assertEqual(conditions[0], (-16808, 75250))
        self.assertEqual(len(conditions), 100000)

    def test_initial_assignment(self):
        assignment = two_sat.initial_assignment(4)
        # print(assignment)
        self.assertEqual(type(assignment), int)

    def test_check_assignment(self):
        assignment = 2+4+8+16
        conditions = [(1, 2),(-1, 2),(-1,-2),(-3,4)]
        condition = two_sat.check_assignment(assignment, conditions)
        print(condition)
        self.assertEqual(condition, 2)
    '''
    def test_modify_assignment(self):
        assignment = 2+4+8+16
        conditions = [(1, 2),(-1, 2),(-1,-2),(-3,4)]
        index = 2
        assignment = two_sat.modify_assignment(assignment, conditions, index)
        self.assertEqual(assignment, 28)

    def test_two_sat(self):
        conditions = [(-1,2), (-2,-3), [-1, -2]]
        print(two_sat.two_sat(conditions))

