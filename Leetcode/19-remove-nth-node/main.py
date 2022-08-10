

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = self.count_elements(head)
        n = length - n

        if n == 0:
            head = head.next
            return head

        cur = head
        prev = None

        for i in range(n):
            prev = cur
            cur = cur.next
        prev.next = cur.next
        return head

    @staticmethod
    def count_elements(head):
        res = 0
        cur = head
        while cur is not None:
            cur = cur.next
            res += 1
        return  res
