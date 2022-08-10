# placeStart
# г. Вологда
# Осокина Вера
class Solution:
    def isPowerOfFour(self, n: int, power=1) -> bool:
        if n == 0:
            return False

        next_power = power + 1
        next_divider = 4 ** next_power
        if n % next_divider == 0:
            n = self.isPowerOfFour(n // next_divider, next_power)

        cur_divider = 4 ** power
        while n % cur_divider == 0:
            n //= cur_divider

        if power == 1:
            return n == 1
        else:
            return n


if __name__ == '__main__':
    print(Solution().isPowerOfFour(17))