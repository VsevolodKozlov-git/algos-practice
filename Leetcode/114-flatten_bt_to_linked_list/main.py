from collections import deque
from enum import Enum


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Oper(Enum):
    add_childs = 0
    make_right = 1


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """

        """
        if root is None:
            return root

        stack = deque()
        stack.append((root, Oper.add_childs))
        while len(stack) != 0:
            node, operation = stack.pop()
            if operation == Oper.add_childs:
                if node.right is not None:
                    stack.append((node.right, Oper.add_childs))
                if node.left is not None:
                    stack.append((node, Oper.make_right))
                    stack.append((node.left, Oper.add_childs))
                last_visited = node

            if operation == Oper.make_right:
                left = node.left
                right = node.right
                node.right = left
                node.left = None
                last_visited.right = right


if __name__ == '__main__':
    t = TreeNode(1)
    left = TreeNode(2)
    t.left = left
    left.left = TreeNode(3)
    left.right = TreeNode(4)

    right = TreeNode(5)
    t.right = right
    right.right = TreeNode(6)
    Solution().flatten(t)
    print('hello')



