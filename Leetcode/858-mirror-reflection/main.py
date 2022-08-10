import math
class Solution:
    def mirrorReflection(self, punches: int, y_cord: int) -> int:
        gcd = math.gcd(punches, y_cord)
        punches //= gcd
        y_cord //= gcd
        # лево
        if punches % 2 == 0:
            return 2
        # право
        else:
            # низ
            if y_cord % 2 == 0:
                return 0
            # верх
            else:
                return 1



if __name__ == '__main__':
    # 45 26 0.05 - out: 2, exp:0
    # 182 155 0.01 - time limit exceeded
    print(Solution().mirrorReflection(45, 26))