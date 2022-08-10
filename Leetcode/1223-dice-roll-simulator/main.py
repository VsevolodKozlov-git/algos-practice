from bisect import bisect_right
import sys
sys.setrecursionlimit(10000)



class Solution:
    def __init__(self):
        self.dp = {}
        self.coding_map = self.get_coding_map()

    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        roll_hash = self.encode(rollMax)
        return self.recursive(n, roll_hash)

    @staticmethod
    def get_coding_map():
        coding_map = []
        val = 0
        for i in range(17):
            coding_map.append(val)
            val = val * 6 + 1
        return coding_map

    def encode(self, rollMax):
        res = 0
        for roll in rollMax:
            res += self.coding_map[roll]
        return res


    def recursive(self, n, roll_hash: int):
        dp_ans = self.dp.get((n, roll_hash), None)
        if dp_ans is not None:
            return dp_ans

        if n == 1:
            return self.get_non_zero(roll_hash)

        res = 0
        i_substractor = bisect_right(self.coding_map, roll_hash) - 1
        remained_hash = roll_hash
        while remained_hash > 0:
            remained_sub = self.coding_map[i_substractor]
            if remained_hash >= remained_sub:
                while_sub = self.coding_map[i_substractor] - self.coding_map[i_substractor - 1]
                while remained_hash >= remained_sub:
                    remained_hash -= remained_sub
                    res += self.recursive(n-1,  roll_hash - while_sub)
            i_substractor -= 1

        self.dp[(n, roll_hash)] = res
        return res

    def get_non_zero(self, roll_hash):
        res = 0
        i_sub = bisect_right(self.coding_map, roll_hash) - 1
        while i_sub > 0 and roll_hash > 0:
            sub = self.coding_map[i_sub]
            while roll_hash >= sub:
                roll_hash -= sub
                res += 1
            i_sub -= 1
        return res

    def get_vals(self, roll_hash):
        res = []
        i_sub = bisect_right(self.coding_map, roll_hash) - 1
        while i_sub > 0 and roll_hash > 0:
            sub = self.coding_map[i_sub]
            while roll_hash >= sub:
                roll_hash -= sub
                res.append(i_sub)
            i_sub -= 1
        return res


if __name__ == '__main__':
    n=3
    rollMax = [1,1,1,2,2,3]

    n = 2
    rollMax = [1, 1, 1, 1, 1, 2]

    print(Solution().dieSimulator(n, rollMax))