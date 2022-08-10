from typing import List
from queue import PriorityQueue
from bisect import bisect_right

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()

        pairs_filtered = []
        prev_start = float('inf')
        for i, pair in enumerate(pairs):
            start = pair[0]
            if start != prev_start:
                pairs_filtered.append(pair)
            prev_start = start

        n = len(pairs_filtered)
        starts = [i[0] for i in pairs_filtered]
        chains = [0] * n
        max_chain = 0

        for i in range(n-1, -1, -1):
            start, end = pairs_filtered[i]
            max_ind = bisect_right(starts, end, lo=i+1)
            if max_ind >= n:
                chain_cur = 1
            else:
                chain_cur = chains[max_ind] + 1

            if chain_cur > max_chain:
                max_chain = chain_cur

            chains[i] = max_chain


        return max_chain


if __name__ == '__main__':
    pairs = [[7,9],[4,5],[7,9],[-7,-1],[0,10],[3,10],[3,6],[2,3]]
    print(Solution().findLongestChain(pairs))