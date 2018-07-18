import unittest
import two_sat

class Test_two_sat(unittest.TestCase):

    def test_get_conditions(self):
        conditions = two_sat.get_conditions("2sat1.txt")
        self.assertEqual(conditions[0], (-16808, 75250))
        self.assertEqual(len(conditions), 100000)

    def test_initial_assignment(self):
        assignment = two_sat.initial_assignment(4)
        self.assertEqual(len(assignment), 4)
        self.assertEqual(type(assignment[0]), bool)

    def test_check_assignment(self):
        assignment = [True, True, True]
        conditions1 = [(1,3), (1,2)]
        conditions2 = [(-1,2), (-2,-3)]
        cns1 = two_sat.check_assignment(assignment, conditions1)
        cns2 = two_sat.check_assignment(assignment, conditions2)
        self.assertEqual(cns1, [])
        self.assertEqual(cns2, [1])

    def test_modify_assignment(self):
        assignment = [True, True, True]
        conditions = [(-1,2), (-2,-3)]
        cns = [1]
        two_sat.modify_assignment(assignment, conditions, cns)
        self.assertNotEqual(assignment[2], True)

    def test_two_sat(self):
        conditions = [(-1,2), (-2,-3), [-1, -2]]
        print(two_sat.two_sat(conditions))
