from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        seq = {}
        for i, num in enumerate(nums):
            mx = seq.get(num, 1)
            for prev_num in nums[:i]:
                if prev_num < num:
                    prev_length = seq.get(prev_num, 0)
                    cur_length = prev_length + 1
                    if cur_length > mx:
                        mx = cur_length
            seq[num] = mx
            if mx > res:
                res = mx
        return res


if __name__ == '__main__':
    nums = [3, 4, 1, 2, 3, 5, 4, 5]
    nums = [10,9,2,5,3,7,101,18]
    nums = [0,1,0,3,2,3]
    print(Solution().lengthOfLIS(nums))