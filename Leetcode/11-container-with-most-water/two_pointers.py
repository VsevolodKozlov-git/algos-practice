from typing import List
class Solution:
    a = []
    res = 0


    def maxArea(self, a: List[int]) -> int:
        self.a = a
        i = 0
        j = len(a) - 1
        self.res = self.get_val(i, j)
        while j > i:
            i = self.better_i(i, j)
            self.res = max(self.res, self.get_val(i, j))
            j -= 1
        return self.res

    def get_val(self, i, j):
        return min(self.a[i], self.a[j]) * abs(i - j)

    def better_i(self, i, j):
        new_i = i
        while self.get_val(new_i, j) <= self.res:
            new_i += 1
            if new_i == len(self.a):
                return i
        else:
            return new_i

    def better_j(self, i, j):
        new_j = j
        while self.get_val(i, new_j) <= self.res:
            new_j -= 1
            if new_j < 0:
                return j
        else:
            return new_j


if __name__ == '__main__':
    height = [i for i in range(1, 6)]
    print(Solution().maxArea(height))