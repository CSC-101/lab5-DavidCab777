import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add1(self):
        x = data.Time(13,12,10)
        y = data.Time(10,10,50)
        result = lab5.time_add(x,y)
        expected = '23, 23, 0'
        self.assertEqual(result == expected)

    def test_time_add2(self):
        x = data.Time(10,20,30)
        y = data.Time(10,30,50)
        result = lab5.time_add(x,y)
        expected = '20, 51, 20'
        self.assertEqual(result == expected)
    # Part 4
    def test_is_descending1(self):
        input = [1.1,2.9,3.14,2.4,102,10.9]
        result = lab5.is_descending(input)
        expected = [102,10,9,3.14,2.9,2.4,1.1]
        if result == expected:
            return print("descending order", result)

    def test_is_descending2(self):
        input = [10.1,20.2,40]
        result = lab5.is_descending(input)
        expected = [40,20.2, 10.1]
        if result == expected:
            return print("descending order", result)

    # Part 5
    def test_largest_between1(self):
        lista = [1,2,4,3,5,0]
        result = lab5.largest_between(lista, 1, 3)
        expected = 2
        self.assertEqual(result == expected)

    def test_largest_between2(self):
        lista = [2,3,4,1,9,8,9,10]
        result = lab5.largest_between(lista, 3, 7)
        expected = 10
        self.assertEqual(result == expected)


    # Part 6
    def test_furthest_from_origin1(self):
        list_of_points = [data.Point(1,2), data.Point(2,4), data.Point(3,9)]
        result = lab5.furthest_from_origin(list_of_points)
        expected = (3, 9)
        self.assertEqual(result == expected)

    def test_furthest_from_origin2(self):
        list_of_points = [data.Point(2,4), data.Point(3,5), data.Point(4,10)]
        result = lab5.furthest_from_origin(list_of_points)
        expected = (4, 10)
        self.assertEqual(result == expected)





if __name__ == '__main__':
    unittest.main()
