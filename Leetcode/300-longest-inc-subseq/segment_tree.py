from sys import maxsize
INT_MIN = -maxsize

def construct_segment_tree(a: list, n: int):
    global segtree

    # assign values to leaves of the segment tree
    for i in range(n):
        segtree[n + i] = a[i]

    # assign values to internal nodes
    # to compute maximum in a given range */
    for i in range(n - 1, 0, -1):
        segtree[i] = max(segtree[2 * i], segtree[2 * i + 1])

def update(pos: int, value: int, n: int):
    global segtree

    # change the index to leaf node first
    pos += n

    # update the value at the leaf node
    # at the exact index
    segtree[pos] = value

    while pos > 1:

        # move up one level at a time in the tree
        pos //= 2

        # update the values in the nodes in
        # the next higher level
        segtree[pos] = max(segtree[2 * pos], segtree[2 * pos + 1])

def range_query(left: int, right: int, n: int) -> int:
    global segtree

    # Basically the left and right indices will move
    # towards right and left respectively and with
    # every each next higher level and compute the
    # maximum at each height.
    # change the index to leaf node first
    left += n
    right += n

    # initialize maximum to a very low value
    ma = INT_MIN
    while left < right:

        # if left index in odd
        if left & 1:
            ma = max(ma, segtree[left])

            # make left index even
            left += 1

        # if right index in odd
        if right & 1:

            # make right index even
            right -= 1

            ma = max(ma, segtree[right])

        # move to the next higher level
        left //= 2
        right //= 2
    return ma

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 1


        num_sorted_ind = {}
        l_sort = 0
        prev_num = float('inf')
        for num in  sorted(nums):
            if num != prev_num:
                num_sorted_ind[num] = l_sort
                l_sort += 1
                prev_num = num

        sequences = [0] * l_sort
        n = len(sequences)
        global segtree
        segtree = [0] * (2 * n)
        construct_segment_tree(sequences, n)

        for i, num in  enumerate(nums):
            sorted_ind = num_sorted_ind[num]
            if sorted_ind == 0:
                new_val = 1
            else:
                mx_val = range_query(0, sorted_ind, n) + 1
                cur_val = range_query(sorted_ind, sorted_ind+1, n)

                new_val = max(mx_val, cur_val)
            update(sorted_ind, new_val, n)
            if new_val > res:
                res = new_val
        return res


if __name__ == '__main__':
    print(Solution().lengthOfLIS([1, 2, 3]))