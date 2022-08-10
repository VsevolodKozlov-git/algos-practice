from queue import PriorityQueue
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        queue = PriorityQueue()
        queue.put((matrix[0][0], 0, 0))
        n_order = 0
        while not queue.empty():
            number, row, col = queue.get()
            n_order += 1
            if n_order == k:
                return number
            else:
                add_to_queue = [(row+1, col)]
                if row == 0:
                    add_to_queue.append((row, col+1))
                for new_row, new_col in add_to_queue:
                    if new_row <  n_rows and new_col < n_cols:
                        new_val = matrix[new_row][new_col]
                        queue.put((new_val, new_row, new_col))


if __name__ == '__main__':
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    print(Solution().kthSmallest(matrix, k))