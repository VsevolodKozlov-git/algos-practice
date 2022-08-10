from typing import List

class CumSumArr:
    def __init__(self, arr):
        self.arr = arr
        self.cum_sum_arr = self.get_cum_sum_arr(arr)

    @staticmethod
    def get_cum_sum_arr(arr: list):
        res = [0] * len(arr)
        res[0] = arr[0]
        for i in range(1, len(arr)):
            res[i] = res[i-1] + arr[i]
        return res

    def get_sum(self, start, end):
        a = self.cum_sum_arr[end]
        if start-1 >= 0:
            b = self.cum_sum_arr[start-1]
        else:
            b = 0
        return  a - b


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        c = CumSumArr(nums)
        for l in range(0, n-2):
            for m in range(l+1, n-1):
                l_s = c.get_sum(0, l)
                m_s = c.get_sum(l+1, m)
                r_s = c.get_sum(m+1, n-1)
                if l_s <= m_s <= r_s:
                    res += 1
        return res

if __name__ == '__main__':
    nums = [0]*5
    print(Solution().waysToSplit(nums))