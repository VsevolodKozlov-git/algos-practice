import unittest
from main import Solution
from time import  perf_counter

isPowerOfFour = Solution().isPowerOfFour


def power_of_four_checker(n):
    if n == 0:
        return False

    while n % 4 == 0 :
        n //= 4
    return  n == 1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        optimized_time = 0
        default_time = 0
        for i in (4**20,4**10):
            start = perf_counter()
            true_result = power_of_four_checker(i)
            default_time += perf_counter() - start

            start = perf_counter()
            actual_result = isPowerOfFour(i)
            optimized_time += perf_counter() - start

            self.assertEqual(true_result, actual_result)

        print(f'default/optimized {default_time/optimized_time}')


if __name__ == '__main__':
    unittest.main()
