from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """

        :param strs:
        :return: Сгруппированные слова с одинаковыми буквами

        1:
            Заведем словарь d где будем хранить какие буквы в каких словах

            Как собирать слова обратно?
            Что делать со словами, буквы которых являются надмножествами
            Что делать со словами, в которых повторяются буквы
        2:
            -Отсортировать буквы в словах
            -Отсортировать  слова в списке strs
            -Циклом идем по strs и если слово отличается, то изменяем указатель


            -Как понять какое слово к какому относится?
            -Отсортировать индексы
        3:
             Использовать уникальное число для каждого набора букв

             Через простые числа получается слишком большое число
        """
        n = len(strs)
        d = {}
        for string in strs:
            key = tuple(sorted(string))
            d[key] = d.get(key, []) + [string]
        return list(d.values())


def get_prime_index(letter):
    return ord(letter) - 97

if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(Solution().groupAnagrams(strs))