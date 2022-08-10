from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return bin_add(nums, 0, len(nums)-1)


def bin_add(arr, l, r):
    if l > r:
        return None
    if l <= r:
        m = (l + r) // 2
        node = TreeNode(arr[m])
        node.left = bin_add(arr, l, m-1)
        node.right = bin_add(arr, m+1, r)
        return node

def bfs(root):
    queue = deque()
    queue.appendleft(root)
    n = 0
    shift = 0
    while len(queue) > 0:
        node = queue.pop()
        n += 1
        if node is not None:
            print(node.val, end=' ')
            queue.appendleft(node.left)
            queue.appendleft(node.right)
        else:
            print('None', end=' ')
        if n == (1 << shift):
            print('\n')
            n = 0
            shift += 1


if __name__ == '__main__':
    nums = [-10,-3,0,5,9]
    root = Solution().sortedArrayToBST(nums)
    bfs(root)