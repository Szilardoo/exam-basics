import odd_avg
import unittest

class Test_odd_avg(unittest.TestCase):

    def test_with_a_list_of_numbers(self):
        self.assertEqual(odd_avg.odd_average([1,2,3,4,5,6,7,8,9]), (1+3+5+7+9)/5)

    def test_with_a_list_of_even_numbers(self):
        self.assertEqual(odd_avg.odd_average([2,4,6,8]), 0)

    def test_with_an_integer(self):
        self.assertEqual(odd_avg.odd_average(0), "That is not a list.")

    def test_with_an_empty_list(self):
        self.assertEqual(odd_avg.odd_average([]), 0)

if __name__ == '__main__':
    unittest.main()
