
class Solution:
    cnt = 0

    def dieSumlator(self, n, rollMax):
        self.dfs(n, rollMax, -1)
        return self.cnt

    def dfs(self, n, rollMax, last):
        if n == 0:
            self.cnt += 1
            return
        for i in range(1, 7):
            if i == last:
                continue

            for j in range(1, rollMax[i-1]+1):
                if (n - j) < 0:
                    break
                self.dfs(n-j, rollMax, i)


if __name__ == '__main__':
    n = 3
    rollMax = [1,1,1,2,2,3]
    print(Solution().dieSumlator(n, rollMax))