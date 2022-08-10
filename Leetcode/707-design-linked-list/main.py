class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next



class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        """

        :param index:
        :return: The value of the indexth node in the linked list.
                 If the index is invalid, return -1.

        """
        cur = self.head
        index_iter = 0
        while cur is not None:
            if index == index_iter:
                return cur.val
            index_iter += 1
            cur = cur.next
        return -1

    def addAtHead(self, val: int) -> None:
        self.head = ListNode(val=val, next=self.head)

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.addAtHead(val)
            return

        tail = self.head
        while tail.next is not None:
            tail = tail.next
        tail.next = ListNode(val=val)

    def addAtIndex(self, index: int, val: int) -> None:
        """

        :param index:
        :param val:
        :return: Add a node of value val before the index node in the linked list.
                 If index equals the length of the linked list,
                 the node will be appended to the end of the linked list.
                 If index is greater than the length, the node will not be inserted.
        """

        if index == 0:
            self.addAtHead(val)
            return

        cur = self.head
        index_iter = 1
        while cur is not None:
            if index_iter == index:
                insert_node = ListNode(next=cur.next, val=val)
                cur.next = insert_node
                return
            index_iter += 1
            cur = cur.next

    def deleteAtIndex(self, index: int) -> None:
        """

        :param index:
        :return:

        """
        if index == 0:
            self.head = self.head.next
            return

        cur = self.head
        index_iter = 1

        while cur is not None and cur.next is not None:
            if index_iter == index:
                if cur.next is not None:
                    cur.next = cur.next.next
                else:
                    cur.next = None
            cur = cur.next
            index_iter += 1




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

if __name__ == '__main__':
    link_list = MyLinkedList()
    link_list.addAtHead(1)
    link_list.addAtTail(3)
    link_list.addAtIndex(1, 2)
    print(link_list.get(1))
