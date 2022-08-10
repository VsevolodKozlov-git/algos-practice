class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        :param s: Набор букв большого и маленького регистра
        :return: Длина наибольшего палиндрома, который можно составить из s
        Варианты палиндромов:
        1) Из нечетного кол-ва букв
            Одна буква может повториться нечетное кол-во раз, остальные повторяются четное кол-во
            ccacc
        2) Из четного кол-ва
            Все буквы повторяются четное кол-во раз

        Заводим словарь и в него считаем буквы, потом суммируем четные и добавляем к
        результату наибольшое кол-во нечетных букв
        """
        palindrome_len = 0
        letter_cnt_dict = {}
        for letter in s:
            if letter in letter_cnt_dict:
                letter_cnt_dict[letter] += 1
            else:
                letter_cnt_dict[letter] = 1

        max_odd_cnt = 0
        for cnt in letter_cnt_dict.values():
            if cnt % 2 == 0:
                palindrome_len += cnt
            elif cnt > max_odd_cnt:
                max_odd_cnt = cnt
        palindrome_len += max_odd_cnt
        return palindrome_len

if __name__ == '__main__':

    # print(s)
    print(Solution().longestPalindrome())
