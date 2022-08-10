import unittest
from main import ListNode, MyLinkedList

def convert_list_to_head_tail(l):
    head = ListNode(l[0])
    tail = head
    for val in l[1:]:
        next_node = ListNode(val)
        tail.next = next_node
        tail = next_node
    return head, tail



null = None

def print_linked_list(linked_list):
    cur = linked_list.head
    while cur is not None:
        print(cur.val, end=' ')
        cur = cur.next


class MyTestCase(unittest.TestCase):
    def test_main(self):
        func_names = ['',"addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
        args = [[], [7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]
        expected_returns = [null, null,null,null,null,null,null,null,4,null,null,null]
        self.test_by_func(func_names, args, expected_returns)

        func_names = ["MyLinkedList","addAtTail","get"]
        args = [[],[1],[0]]
        expected_returns = [None, None, 1]
        self.test_by_func(func_names, args, expected_returns)


    def test_by_func(self, func_names, args, expected_returns):
            func_names = func_names[1:]
            args = args[1:]
            expected_returns = expected_returns[1:]
            ll = MyLinkedList()
            for func_name, arg, expected in zip(func_names, args, expected_returns):
                method = getattr(ll, func_name)
                actual = method(*arg)
                self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
