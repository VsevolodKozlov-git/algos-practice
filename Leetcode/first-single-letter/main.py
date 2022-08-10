def first_single_letter(s):
    letters_cnt_dict = {}
    for i in range(len(s)):
        first_letter = s[i]
        for j in range(i+1, len(s)):
            second_letter = s[j]
            if first_letter == second_letter:
                break
        else:
            return  first_letter

if __name__ == '__main__':
    print(first_single_letter('abcab'))
