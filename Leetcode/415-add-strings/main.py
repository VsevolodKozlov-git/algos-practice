class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(sum(map(int, [num1, num2])))


if __name__ == '__main__':
    print(Solution.addStrings('123', '45'))
