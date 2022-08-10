from typing import List
from collections import deque, defaultdict

res_dict = defaultdict(int)

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        merge(arr, L, R)


def merge(arr, L, R):
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            res_dict[L[i]] += j
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1


    first = False
    while i < len(L):
        arr[k] = L[i]
        res_dict[L[i]] += len(R)
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        saved_nums = nums.copy()
        mergeSort(nums)
        res = []
        for num in saved_nums:
            res.append(res_dict[num])
        return res

if __name__ == '__main__':
    print(Solution().countSmaller([-1, -1]))


