from typing import List






class NumArray:

    def __init__(self, nums: List[int]):
        self.inter_tree = IntervalTree(nums)

    def update(self, index: int, val: int) -> None:
        self.inter_tree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return  self.inter_tree.get_sum(left, right)


class Node:
    def __init__(self, start, end, val, parent, left=None, right=None):
        self.start = start
        self.end = end
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right

    def is_equal_index(self, ind):
        return (self.start == self.end) and (self.start == ind)

    def __eq__(self, other):
        return  (self.start == other.start and
                 self.end == other.end and
                 self.val == other.val)


class IntervalTree:
    def __init__(self, arr):
        self.arr = arr
        self.cum_sum_arr = CumSumArr(arr)
        self.root = self.construct_tree()

    def construct_tree(self):
        return self.__constractor(None, 0, len(self.arr)-1)


    def __constractor(self, parent, start, end):
        val = self.cum_sum_arr.get_sum(start, end)
        node = Node(start, end, val, parent)
        mid = (start + end) // 2
        if start != end:
            left_child = self.__constractor(node, start, mid)
            right_child = self.__constractor(node, mid+1, end)
            node.left = left_child
            node.right = right_child
        return node

    def get_sum(self, start, end):
        last_same_node = self.root
        start_node = self.root
        end_node = self.root
        start_found = False
        end_found = False
        while not start_found or not end_found:
            if not start_found:
                start_node = self.find_next(start_node, start)
            start_found = start_node.is_equal_index(start)

            if not end_found:
                end_node = self.find_next(end_node, end)
            end_found = end_node.is_equal_index(end)

            if start_node == end_node:
                last_same_node = start_node

        if (start_node == end_node) and (end_node == last_same_node):
            return start_node.val
        minus_left = 0
        while start_node.parent != last_same_node:
            parent = start_node.parent
            if parent.right == start_node:
                if parent.left is not None:
                    minus_left += parent.left.val
            start_node = parent

        minus_right = 0
        while end_node.parent != last_same_node:
            parent = end_node.parent
            if parent.left == end_node:
                if parent.right is not None:
                    minus_right += parent.right.val
            end_node = parent

        return last_same_node.val - minus_left - minus_right




    @staticmethod
    def find_next(node, ind):
        if node.is_equal_index(ind):
            return node

        mid = (node.start + node.end) // 2
        if ind <= mid:
            node = node.left
        else:
            node = node.right
        return node

    def find(self, ind):
        node = self.root
        while not node.is_equal_index(ind):
            node = self.find_next(node, ind)
        return  node

    def update(self, ind, new_val):
        node = self.find(ind)
        old_val = node.val
        difference = new_val - old_val
        while node is not None:
            node.val += difference
            node = node.parent


class CumSumArr:
    def __init__(self, arr):
        self.arr = arr
        self.cum_sum_arr = self.get_cum_sum_arr(arr)

    @staticmethod
    def get_cum_sum_arr(arr: list):
        res = [0] * len(arr)
        res[0] = arr[0]
        for i in range(1, len(arr)):
            res[i] = res[i-1] + arr[i]
        return res

    def get_sum(self, start, end):
        a = self.cum_sum_arr[end]
        if start-1 >= 0:
            b = self.cum_sum_arr[start-1]
        else:
            b = 0
        return  a - b