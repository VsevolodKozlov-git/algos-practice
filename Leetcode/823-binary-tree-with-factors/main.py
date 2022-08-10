from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]):
        arr.sort()
        res = 0
        num_trees = {}

        for i, num in enumerate(arr):
            factorization = []
            for j, fac1 in enumerate(arr[:i]):
                if num % fac1 == 0:
                    fac2 = num // fac1
                    if fac1 > fac2:
                        break
                    if fac2 in num_trees:
                        factorization.append((fac1, fac2))

            trees = 1
            for fac1, fac2 in factorization:
                fac_combinations = num_trees[fac1] * num_trees[fac2]
                if fac1 != fac2:
                    fac_combinations *= 2
                trees += fac_combinations

            num_trees[num] = trees
            res += trees
            res %= int(1e9) + 7
        return res


if __name__ == '__main__':
    print(Solution().numFactoredBinaryTrees([2, 3, 4, 6, 8, 12]))