class Solution:
    def longestPalindrome(self, s: str) -> str:
        """

        :param s:
        :return: наибольший палиндром в s

        1: Палиндром (aBa) (aBba)
            - Просто идем по серединам(левый от середины(сначала правый добавляем))
            и если палиндромность нарушена 2 раза, то следующий шаг
            b - ba - aba - abac - eabac(следующая итерация)
            b - bb - abb - abbc
            Прекращаем только когда нарушена полиндромность 2 раза


            Заводим 2 разных цикла:
                -Один идет по четным полиндром
                -Второй по нечетным
                -если ошибка, то прерырваем
                -если больше res, то заменяем
        2:
            Храним только начало, концом является сам индекс
            st = dynamic[i-1]
            если s[st-1] == s[i], то dyan
        """
        n = len(s)
        dynamic = [0] * n
        res = s[0]
        length = 1
        equal = True
        for i in range(1, n):
            st_ind = dynamic[i-1]
            if st_ind > 0 and s[st_ind - 1] == s[i]:
                dynamic[i] = st_ind - 1
                length += 2
            elif s[st_ind] == s[i] and equal:
                dynamic[i] = st_ind
                length += 1
            elif s[st_ind+1] == s[i]:
                dynamic[i] = st_ind + 1

            else:
                dynamic[i] = i
                length = 1
            equal = equal and s[dynamic[i]] == s[i] == s[(dynamic[i] + i) // 2]
            if length > len(res):
                res = s[dynamic[i]: i+1]
        return res


def print_matrix(matr):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in matr]))


if __name__ == '__main__':
    print(Solution().longestPalindrome('aacabdkacaa'))
