class Solution:
    def minDeletions(self, s: str) :
        freq_arr = get_freq_arr(s)
        freq_arr = sorted(freq_arr, reverse=True)

        deletions = 0
        deleted_flag = True
        while deleted_flag:
            deleted_flag = False
            freq_prev = freq_arr[0]
            i = 1
            while i < 26:
                if freq_arr[i] == 0:
                    break
                if freq_prev == freq_arr[i]:
                    while i < 26 and freq_prev == freq_arr[i]:
                        if freq_arr[i] == 0:
                            break
                        freq_arr[i] -= 1
                        deletions += 1
                        deleted_flag = True
                        i += 1
                    freq_prev = freq_arr[i-1]
                else:
                    freq_prev = freq_arr[i]
                    i += 1

        return deletions, freq_arr


def get_freq_arr(s):
    freq_arr = [0] * 26
    for char in s:
        char_order = ord(char) - 97
        freq_arr[char_order] += 1
    return freq_arr


if __name__ == '__main__':
    s = 'abcabc'
    print(Solution().minDeletions(s))