from typing import List

class Solution:
    def maxArea(self, vert_len: int, hor_len: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        v_max_dist = find_max_dist(horizontalCuts, vert_len)
        h_max_dist = find_max_dist(verticalCuts, hor_len)
        return (v_max_dist * h_max_dist) % (int(1e9) + 7)


def find_max_dist(arr, end_val):
    max_dist = arr[0]
    for i in range(1, len(arr)):
        dist = arr[i] - arr[i-1]
        if dist > max_dist:
            max_dist = dist
    dist = end_val - arr[-1]
    if dist > max_dist:
        max_dist = dist
    return max_dist


if __name__ == '__main__':
    print(Solution().maxArea(5, 4, horizontalCuts = [3,1], verticalCuts = [1]))