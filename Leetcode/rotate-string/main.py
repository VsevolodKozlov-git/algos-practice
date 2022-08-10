class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        for shift in range(1, len(s) - 1):
            for ind in range(len(s)):
                shifted_ind = ind - shift
                if goal[ind] != s[shifted_ind]:
                    break
            else:
                return True
        return False
