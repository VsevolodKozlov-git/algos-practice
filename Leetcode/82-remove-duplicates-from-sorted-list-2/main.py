from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """

        :param head:
        :return: Связный список без элементов, который повторяются хотя бы 1 раз
        1:
            имеем prev, preprev, current
            если prev == current, то prevprev.next = current.next
            0 - 1 - 1 - 1
            pp  p   c
            0 1
        """
        head = ListNode(val=head.val-1, next=head)
        cur = head.next
        prev = head
        prev_prev = head
        while cur is not None:
            if cur.val == prev.val:
                while cur is not None and cur.val == prev.val:
                    prev = cur
                    cur = cur.next
                    while_flag = True
                prev_prev.next = cur
                prev = prev_prev
            else:
                prev_prev = prev
                prev = cur
                cur = cur.next
        return head.next


def convert_list_to_head_tail(l):
    head = ListNode(l[0])
    tail = head
    for val in l[1:]:
        next_node = ListNode(val)
        tail.next = next_node
        tail = next_node
    return head, tail


if __name__ == '__main__':
    l = [1, 1, 2, 3, 3, 4, 5]
    head = convert_list_to_head_tail(l)[0]
    head = Solution().deleteDuplicates(head)
    while head:
        print(head.val, end=' ')
        head = head.next
