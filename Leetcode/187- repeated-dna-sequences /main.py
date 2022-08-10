from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """

        :param s: состоит из A C G t
        :return: повторяющиейся подстроки длины 10

        1:
            -Т. к. длина 10, то можно использовать скользящее окно
            -Как сравнивать строки

        """
        n = len(s)
        d = {}
        for i in range(n-9):
            substr = s[i:i+10]
            d[substr] = d.get(substr, 0) + 1
        return [key for key in d if d[key] > 1]

if __name__ == '__main__':
    s = "AAAAAAAAAAA"
    print(len(s))
    print(Solution().findRepeatedDnaSequences(s))