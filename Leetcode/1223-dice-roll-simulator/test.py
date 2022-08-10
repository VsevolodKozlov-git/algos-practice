from bisect import bisect_left
import sys
sys.setrecursionlimit(10000)



class Solution:
    def __init__(self):
        self.dp = {}

    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        return self.recursive(n, tuple(rollMax))

    def recursive(self, n, rollMax:tuple):
        dp_ans = self.dp.get((n, rollMax), None)
        if dp_ans is not None:
            return dp_ans

        if n == 1:
            return self.get_non_zero(rollMax)

        rollMax_l = list(rollMax)
        res = 0
        for i in range(6):
            rolls = rollMax[i]
            if rolls == 0:
                continue
            else:
                rollMax_l[i] -= 1
                res += self.recursive(n-1, tuple(rollMax_l))
                rollMax_l[i] += 1
        self.dp[(n, rollMax)] = res
        if n == 3:
            breakpoint()
        return res

    def get_non_zero(self, hashes):
        res = 0
        for hash in hashes:
            if hash != 0:
                res += 1
        return  res

if __name__ == '__main__':
    n=3
    rollMax = [1,1,1,2,2,3]

    # n = 2
    # rollMax = [0, 0, 0, 0, 0, 2]

    print(Solution().dieSimulator(n, rollMax))