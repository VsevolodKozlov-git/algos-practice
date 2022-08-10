import unittest
from  min_moves_to_seat import  minMovesToSeat

class MyTestCase(unittest.TestCase):
    def test_simple(self):
        seats = [3, 1, 5]
        students = [2, 7, 4]
        real = minMovesToSeat(seats=seats, students=students)
        expected = 4
        self.assertEqual(real, expected)

        seats = [4,1,5,9]
        students = [1,3,2,6]
        real = minMovesToSeat(seats=seats, students=students)
        expected = 7
        self.assertEqual(real, expected)




if __name__ == '__main__':
    unittest.main()
