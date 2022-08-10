from typing import List
from collections import Counter


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        master_dict = create_master_dict(words2)
        return list(filter(lambda word: is_match(word, master_dict), words1))


def create_master_dict(words):
    master_dict = {}
    for subset in words:
        counter_dict = Counter(subset)
        for letter, cnt in counter_dict.items():
            if master_dict.setdefault(letter, cnt) < cnt:
                master_dict[letter] = cnt
    return master_dict


def is_match(word, master_dict):
    word_dict = Counter(word)
    for letter, master_cnt in master_dict.items():
        word_cnt = word_dict.get(letter, 0)
        if word_cnt < master_cnt:
            return False
    return True


if __name__ == '__main__':
    print(Solution().wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]))