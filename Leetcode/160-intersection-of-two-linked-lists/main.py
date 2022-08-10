from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """

        :param headA:
        :param headB:
        :return:

        1:
            Использовать два множества для перекрестного поиска пересечения
        2:
            Есть решение без дополнительной памяти

            -С какого-то элемента числа начнут повторяться
            -Может дойти до хвоста и что-то делать от обратного?
            -А что если зациклить связный список(Тогда нам придется его разцикливать)
            -Хотелось бы знать откуда ты пришел, но это подрозумевает использование памяти
            -А что если дойти до хвоста, сравнить его, если равны, то зацикливаем
             и начинаем бегать указателями
            -
        3:
            Идем в обоих случаях до хвоста и если они равны, то пересечение очевидно есть
            Потом идем до предпоследнего элемента и если они равны, то поднимаемся выше и так до
            тех пор пока элементы не будут равны, тогда возвращаем элемент до которого мы шли в этот раз

        4:


        """
        setA = set()
        setB = set()
        nodeA = headA
        nodeB = headB
        while (nodeA is not None) or (nodeB is not None):
            if nodeA is not None:
                if nodeA in setB:
                    return nodeA
                setA.add(nodeA)
                nodeA = nodeA.next

            if nodeB is not None:
                if nodeB in setA:
                    return nodeB
                setB.add(nodeB)
                nodeB = nodeB.next

