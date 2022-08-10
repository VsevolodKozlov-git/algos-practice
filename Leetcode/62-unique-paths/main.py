from math import factorial

class Solution:
    def uniquePaths(self, rows: int, cols : int) -> int:
        m = rows - 1
        n = cols - 1
        res = 1
        for i in range(max(m,n)+1, m+n+1):
            res *= i
        res //= factorial(min(m, n))
        return res


if __name__ == '__main__':
    print(Solution().uniquePaths(3, 2))