from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        nums.sort()

        # find first non_negative(zero or more)
        non_negative_start = 0
        while nums[non_negative_start] < 0:
            non_negative_start += 1

        # fix one negative and find
        prev = None
        for neg in nums[:non_negative_start]:
            if prev == neg:
                continue
            prev = neg
            for first_pos_ind in range(non_negative_start, len(nums)-1):
                for second_pos_ind in range(first_pos_ind+1, len(nums)):
                    first_pos = nums[first_pos_ind]
                    second_pos = nums[second_pos_ind]
                    triplet = [neg, first_pos, second_pos]
                    sm = sum(triplet)
                    if sm == 0:
                        res.append(triplet)
                    elif sm > 0:
                        break

        for pos in nums[non_negative_start:]:
            if prev == pos:
                continue
            prev = pos
            for first_neg_ind in range(0, non_negative_start-1):
                for second_neg_ind in range(first_neg_ind+1, non_negative_start):
                    first_neg = nums[first_neg_ind]
                    second_neg = nums[second_neg_ind]
                    triplet = [pos, first_neg, second_neg]
                    sm = sum(triplet)
                    if sm == 0:
                        res.append(triplet)
                    elif sm > 0:
                        break

        if len(nums) >= 3 and all(map( lambda x:x==0, nums[non_negative_start:non_negative_start+3])):
            res.append([0, 0, 0])

        return res

def find_all_sums(num_start, num_end, pair_start, pair_end)