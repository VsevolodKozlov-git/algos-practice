from typing import Optional


class ListNode:
    def __init__(self, x):
        self.next = None
        self.val = x


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """

        :param head:
        :return: элемент, на который происходит зацикливание

        O(1) - память
        Не изменять исходный список
        1:
            Нам надо как-то понять что числа повторяются
            3 2 0 -4   2 0 -4   2 0 -4

            xor через некоторый промежуток будет давать одно и то же число, но и что с того?

        2:
            Так как память константна, то мы можем иметь только переменные или списки, ограниченной длины
            Какие это могут быть переменные?
            Зацикливание => цифры повторяются => суммы повторяются
            Как мы можем подумать визуально о зацикливании

            Суммы xor тоже могут повторяться  не только в связи с зацикливанием

            а нельзя ли складывать xorom уникальный идентификаторы нод


            До зацикливания все ок, а потом когда цикл закончился опять вылезло это число
        3:
            Без константной памяти

            Создаем словарь где каждой ноде соответсвует ее порядковый номер

        4:

        """
        cur = head




def convert_list_to_head_tail(l):
    head = ListNode(l[0])
    tail = head
    for val in l[1:]:
        next_node = ListNode(val)
        tail.next = next_node
        tail = next_node
    return head, tail


def test(l):
    sm = 0
    for i in l:
        sm ^= i
        print(i, sm)