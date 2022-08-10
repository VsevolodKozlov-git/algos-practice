import unittest
from random import choice
from time import perf_counter_ns

def checker(s):
    letters_cnt_dict = {}
    for letter in s:
        if letter not in letters_cnt_dict:
            letters_cnt_dict[letter] = 0
        letters_cnt_dict[letter] += 1

    for letter in s:
        if letters_cnt_dict[letter] == 1:
            return letter





class MyTestCase(unittest.TestCase):
    def test_something(self):
        tests = 1000
        checker_time = 0
        alg_time = 0
        for _ in range(tests):
            random_str = self.generate_stings()

            start = perf_counter_ns()
            real = checker(random_str)
            checker_time += perf_counter_ns() - start

            start = perf_counter_ns()
            actual = checker(random_str)
            alg_time += perf_counter_ns() - start
            self.assertEqual(real, actual)

        print(f'checker_time / alg_time(bigger=better)', {checker_time/alg_time})

    @staticmethod
    def generate_stings():
        length = 7
        letters_pool = list('abcdefgh')
        random_str = ''.join((choice(letters_pool) for _ in range(length)))
        # add '9' to ensure that we have at least one single number
        return random_str + '9'



if __name__ == '__main__':
    unittest.main()
