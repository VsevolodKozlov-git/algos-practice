from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        n *= 2
        prev = [('', 0)]
        cur = []
        for i in range(n):
            rem = n - i
            for prev_str, opened in prev:
                if opened + 1 <= rem - 1:
                    cur.append((prev_str+'(', opened+1))
                if opened > 0 :
                    cur.append((prev_str+')', opened-1))
            prev = cur
            cur = []
        return [i[0] for i in prev]


if __name__ == '__main__':
    print(Solution().generateParenthesis(1))

