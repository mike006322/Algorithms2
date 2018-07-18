import unittest
import two_sat

class Test_two_sat(unittest.TestCase):

    def test_make_graph(self):
        result = two_sat.make_graph('test1.txt')
        print(result[1])
        #self.assertEqual(result[0], 100000)
        #self.assertGreater(len(result[1]), result[0])

    def test_two_sat(self):
        file = 'test1.txt'
        print(two_sat.two_sat(file))

