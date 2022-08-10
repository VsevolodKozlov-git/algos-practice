from typing import List
from collections import defaultdict


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        correct_words = []
        for word in words:
            pattern_word = defaultdict(lambda: None)
            word_pattern = defaultdict(lambda: None)
            for i in range(len(pattern)):
                letter_word = word[i]
                letter_pat = pattern[i]
                if letter_pat in pattern_word:
                    if letter_word != pattern_word[letter_pat]:
                        break
                else:
                    pattern_word[letter_pat] = letter_word
                if letter_word in word_pattern:
                    if letter_pat != word_pattern[letter_word]:
                        break
                else:
                    word_pattern[letter_word] = letter_pat
            else:
                correct_words.append(word)
        return correct_words

if __name__ == '__main__':
    print(Solution().findAndReplacePattern(
        words = ["abc","deq","mee","aqq","dkd","ccc"],
        pattern = "abb"))