import unittest
from main import Solution

sortColors = Solution().sortColors

class MyTestCase(unittest.TestCase):
    def test_sortColors(self):
        self.test_nums([2, 0, 2, 1, 1, 0])
        self.test_nums([2,0,1])
        self.test_nums([0, 2, 0, 0, 2, 0, 2, 2, 0, 0, 2, 2, 0])
        self.test_nums([1, 2, 0])
        self.test_nums([1, 2, 2, 0, 0])

    def test_nums(self, nums):
        expected = sorted(nums)
        actual = sortColors(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
