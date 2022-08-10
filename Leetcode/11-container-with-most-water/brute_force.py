from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = Aproximation().maxArea(height)
        for i, val_i in enumerate(height):
            for j, val_j in enumerate(height[:i]):
                if (i - j) * val_i <= res:
                    break
                new_res = abs(i-j)* min(val_i, val_j)
                res = max(res, new_res)
        return res

class Aproximation:
    a = []
    res = 0
    def maxArea(self, a: List[int]) -> int:
        self.a = a
        i = 0
        j = len(a) - 1
        self.res = self.get_val(i, j)
        while True:
            new_i = self.better_i(i, j)
            new_j = self.better_j(new_i, j)
            unchanged_flag = new_i == i and new_j == j
            i = new_i
            j = new_j
            self.res = self.get_val(i, j)
            if unchanged_flag:
                break
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
    height = [1,8,6,2,5,4,8,3,7]
    height = [i for i in range(int(1e5))]
    print(Solution().maxArea(height))