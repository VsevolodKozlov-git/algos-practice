from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            num = nums[i]
            repeated = False
            for j in range(i+1, length):
                if num == nums[j]:
                    repeated = True
                    break
            if not repeated:
                return num


if __name__ == '__main__':
    Solution().singleNumber([2, 2, 1])
