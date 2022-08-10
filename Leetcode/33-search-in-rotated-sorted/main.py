from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        if nums[-1] >= nums[0]:
            return binary_search(nums, 0, n-1, target)


        border_val = nums[-1]
        k = find_k(nums, border_val)
        if target <= border_val:
            return binary_search(nums, k, n-1, target)
        else:
            return binary_search(nums, 0, k-1, target)


def find_k(nums, border_val):
    start = 0
    end = len(nums)
    while start+1 != end:
        mid = (start + end) // 2
        if nums[mid] > border_val:
            start = mid
        else:
            end = mid
    return end


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


if __name__ == '__main__':
    nums = [4, 0, 1, 2, 3]
    target = 10
    nums=[1, 3]
    target = 1
    print(Solution().search(nums, target))
