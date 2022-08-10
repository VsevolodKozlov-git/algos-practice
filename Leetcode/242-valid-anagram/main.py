class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = [0] * 26
        for letter in s:
            index = ord(letter) - 97
            letters[index] += 1
        for letter in t:
            index = ord(letter) - 97
            letters[index] -= 1
        return all(map(lambda x: x == 0, letters))

if __name__ == '__main__':
    print(Solution().isAnagram("aa", "aa"))