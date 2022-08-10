from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """

        :param l1: linked list 1
        :param l2: linked list 2
        :return: sum

        1:
            -Идем циклом до тех пор пока оба списка не закончатся
            -Если один из списков закончился, то его значение = 0
            -Если сумма больше 9, то one_flag = True
            -Записываем сумму в результирующий связный список res
            -У нас есть head(начало связного списка) и tail(нода по которой итерируем)
             И в конце tail должен ссылаться на последний элемент
        """

        head = ListNode()
        tail = None
        one_flag = False
        while (l1 is not None) or (l2 is not None):
            if tail is None:
                tail = head
            else:
                tail.next = ListNode()
                tail = tail.next

            if l1 is None:
                l1_val = 0
            else:
                l1_val = l1.val
            if l2 is None:
                l2_val = 0
            else:
                l2_val = l2.val
            sm = l1_val + l2_val + one_flag
            one_flag = sm > 9
            tail.val = sm % 10

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if one_flag:
            tail.next = ListNode(1)
        return head


def convert_to_list_node(l):
    head = ListNode(l[0])
    tail = head
    for val in l[1:]:
        tail.next = ListNode(val)
        tail = tail.next
    return head


def print_list_node(node):
    while node is not None:
        print(node.val)
        node = node.next



l1 = convert_to_list_node([0])
l2 = convert_to_list_node([0])
sm = Solution().addTwoNumbers(l1, l2)