import unittest
from main import IntervalTree


def print_tree(node , lvl=0, left=None):
    if node is None:
        return
    if left is None:
        sign = 'X'
    elif left:
        sign = 'L'
    else:
        sign = 'R'
    print('\t'*lvl+sign+'-'+str(node.val))
    print_tree(node.left, lvl+1, left=True)
    print_tree(node.right, lvl+1, left=False)


class MyTestCase(unittest.TestCase):
    def test_tree_constraction(self):
        arr = [1, 2, 4, 1, 3, 5]
        t = IntervalTree(arr)
        t.update(1, 10)
        print(t.get_sum(0, 4))

    def test_smth(self):
        arr = [0, 9, 5, 7, 3]
        t = IntervalTree(arr)
        t.update(4, 5)
        t.update(1, 7)
        t.update(0, 8)
        expected = 12
        real = t.get_sum(1, 2)
        self.assertEqual(expected, real)


if __name__ == '__main__':
    unittest.main()
