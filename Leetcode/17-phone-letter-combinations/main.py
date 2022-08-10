from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_letters = {'2': 'abc', '3': 'def',
                         '4': 'ghi', '5': 'jkl',
                         '6': 'mno', '7': 'pqrs',
                         '8': 'tuv',
                         '9': 'wxyz'}
        if not digits:
            return []
        old_letters = ['']
        cur_letters = []
        for digit in digits:
            next_letters = digit_letters[digit]
            for old_letter in old_letters:
                for next_letter in next_letters:
                    cur_letters.append(old_letter+next_letter)
            old_letters = cur_letters
            cur_letters = []
        return old_letters


if __name__ == '__main__':
    print(Solution().letterCombinations('23'))
