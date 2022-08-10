from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # first we throw zeros at start and ones to end
        zeros_end = 0
        ones_end = 0
        twos_start = len(nums) - 1
        while ones_end <= twos_start:
            val = nums[ones_end]
            if val == 0:
                swap_elements(nums, zeros_end, ones_end)
                zeros_end += 1
                ones_end += 1
            if val == 1:
                # don't do anything
                ones_end += 1
            if val == 2:
                swap_elements(nums, ones_end, twos_start)
                twos_start -= 1
        return nums

def swap_elements(l, el1, el2):
    l[el1], l[el2] = l[el2], l[el1]

def sort_two_colors(nums):
    pass



