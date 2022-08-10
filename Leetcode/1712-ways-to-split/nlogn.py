from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        c = self.get_cum_sum_arr(nums)
        for l in range(0, n-2):
            # right - left
            m_min = bisect_left(c, 2*c[l], lo=l+1)
            m_max= bisect_right(c, (c[-1]+c[l])/2, hi=n-1)
            if m_max - m_min <= 0:
                continue
            res += m_max - m_min
        return res % (int(1e9)+7)

    @staticmethod
    def get_cum_sum_arr(arr: list):
        res = [0] * len(arr)
        res[0] = arr[0]
        for i in range(1, len(arr)):
            res[i] = res[i-1] + arr[i]
        return res



if __name__ == '__main__':
    nums = [0]* 5
    print(Solution().waysToSplit(nums))