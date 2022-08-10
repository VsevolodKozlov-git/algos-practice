
class Solution:
    def __init__(self):
        self.dp = {}
        self.rollMax = []

    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        self.rollMax = rollMax
        return self.helper(n, -1, -1)


    def helper(self, n, rem, start):
        if n == 0:
            return 0
        if n == 1:
            if rem > 0:
                return 6
            else:
                return 5

        if (n, rem, start) in self.dp:
            return self.dp[(n, rem, start)]



        found = False
        res = 0
        for roll in self.rollMax:
            if roll == start and not found:
                found = True
                if rem > 0:
                    res += self.helper(n-1, rem-1, start)
            else:
                res += self.helper(n-1, roll-1, roll)
                res %= (int(1e9) + 7)
        self.dp[(n, rem, start)] = res
        return res


if __name__ == '__main__':
    n = 20
    rollMax = [8,5,10,8,7,2]
    # n = 3
    # rollMax = [1,1,1,2,2,3]
    print(Solution().dieSimulator(n, rollMax))