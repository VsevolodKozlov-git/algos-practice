from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        cur_index = m + n -1
        m -= 1
        n -= 1
        while m >= 0  or n >= 0:
            if nums1[m] > nums2[n]:
                nums1[cur_index] = nums1[m]
                m -= 1
            else:
                nums1[cur_index] = nums2[n]
                n -= 1
            cur_index -= 1
        if n >= 0:
            nums1[:n+1] = nums2[:n+1]


if __name__ == '__main__':
    nums1=[1,2,3,0,0,0]
    Solution().merge(nums1,3,[2,5,6],3)
    print(nums1)



