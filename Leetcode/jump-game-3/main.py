from typing import List
from collections import deque


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        new_nodes = deque()
        new_nodes.append(start)
        while new_nodes:
            node = new_nodes.pop()
            jump_length = arr[node]
            # mark as visited
            arr[node] = -1

            if jump_length == 0:
                return True

            for new_node in [node + jump_length, node - jump_length]:
                if (0 <= new_node < len(arr)) and (arr[new_node] != -1):
                    new_nodes.append(new_node)
        return False


