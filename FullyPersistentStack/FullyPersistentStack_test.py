import unittest
import random
from FullyPersistentStack import FullyPersistentStack


class TestFullyPersistentStackMethods(unittest.TestCase):

    def test_basic(self):
        v = FullyPersistentStack()
        w = v.append(1)
        val, x = w.pop()
        self.assertEqual(val, 1)

    def test_initialize(self):

        input = [1, 2, 3]
        v = FullyPersistentStack(input)
        self.assertEqual(len(v), len(input))
        self.assertEqual(v.to_list(), input)
        self.assertEqual(v.peek(), input[-1])
        while input:
            val, v = v.pop()
            self.assertEqual(val,
                             input.pop())

    def test_list(self):
        v1 = FullyPersistentStack()
        v2 = v1.append(2)
        v3 = v2.append(3)
        self.assertEqual(v1.to_list(), [])
        self.assertEqual(v2.to_list(), [2])
        self.assertEqual(v3.to_list(), [2, 3])

        v4 = v2.append(4)
        self.assertEqual(v4.to_list(), [2, 4])

    def test_random(self):

        input = [1, 2, 3]
        v1 = FullyPersistentStack(input)
        nodes = []
        lists = []

        nodes.append(v1)
        lists.append(input)

        TRIALS = 100
        for _ in range(TRIALS):
            x = random.randint(-100, 100)
            current_node = random.choice(nodes)
            current_list = current_node.to_list()
            current_list.append(x)
            lists.append(current_list)
            nodes.append(current_node.append(x))

        for _ in range(TRIALS):
            current_node = random.choice(nodes)
            current_list = current_node.to_list()
            if len(current_list) > 0:
                current_list.pop()
                _, new = current_node.pop()
                lists.append(current_list)
                nodes.append(new)

        for list, node in zip(lists, nodes):
            self.assertEqual(list, node.to_list())


if __name__ == '__main__':
    unittest.main()
