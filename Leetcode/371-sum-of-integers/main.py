class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a < 0 and b < 0:
            return -self.plus(-a, -b)
        elif a >= 0 and b >= 0:
            return self.plus(a, b)
        elif a < 0:
            if abs(a) < abs(b):
                return self.minus(b, -a)
            else:
                return -self.minus(-a, b)
        else:
            if abs(a) < abs(b):
                return -self.minus(-b, a)
            else:
                return self.minus(a, -b)


    @staticmethod
    def plus(a, b):
        res = a
        add = b
        while add != 0:
            tmp = res
            res ^= add
            add &= tmp
            add <<= 1
        return res

    def minus(self, a, b):
        res = a
        min = b
        while min > 0:
            tmp = res
            res ^= min
            min = ~tmp & min
            min <<= 1
        return res


if __name__ == '__main__':

    print(Solution().plus(20, -10))