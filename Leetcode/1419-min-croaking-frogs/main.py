class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        max_frogs = 0
        frogs = 0
        d_waiting = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
        d_next = {'c': 'r', 'r': 'o', 'o': 'a', 'a': 'k', 'k': None}

        for letter in croakOfFrogs:
            if letter not in d_waiting:
                return -1
            if letter == 'c':
                d_waiting['r'] += 1
                frogs += 1
            else:
                waiting_frogs = d_waiting[letter]
                if waiting_frogs == 0:
                    return -1
                else:
                    d_waiting[letter] -= 1
                    next_letter = d_next[letter]
                    if next_letter is None:
                        frogs -= 1
                    else:
                        d_waiting[next_letter] += 1
            if frogs > max_frogs:
                max_frogs = frogs
        if sum(d_waiting.values()) == 0:
            return max_frogs
        else:
            return -1


if __name__ == '__main__':
    print(Solution().minNumberOfFrogs("croakcroa"))