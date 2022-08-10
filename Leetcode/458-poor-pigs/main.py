class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        pigs = 0
        tests = minutesToTest // minutesToDie
        while (tests + 1) ** pigs < buckets:
            pigs += 1
        return pigs


if __name__ == '__main__':
    print(Solution().poorPigs(9, 15, 40))