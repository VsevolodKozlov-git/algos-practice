class Solution(object):
    def maxSubArray(self, nums):
        max_sum = 0
        max_sum_with_num = 0
        for num in nums:
            if max_sum_with_num < 0:
                max_sum_with_num = 0
            max_sum_with_num += num
            if max_sum_with_num > max_sum:
                max_sum = max_sum_with_num
        return max_sum

