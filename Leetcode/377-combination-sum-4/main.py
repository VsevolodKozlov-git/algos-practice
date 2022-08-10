from typing import List
import sys
sys.setrecursionlimit(2000)

class Solution:
    def __init__(self):
        self.dp = [-1] * 1001
        self.dp[0] = 1
        self.nums_sorted = []

    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.nums_sorted = sorted(nums)
        return self.rec(target)

    def rec(self, target):
        if self.dp[target] != -1:
            return self.dp[target]
        res = 0
        for num in self.nums_sorted:
            if num > target:
                break
            res += self.rec(target - num)
        self.dp[target] = res
        return res


if __name__ == '__main__':

    print(Solution().combinationSum4([1,2,3], 5))