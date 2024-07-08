import unittest
import random
from PersistentStack import PersistentStack


class TestPersistentStackMethods(unittest.TestCase):

    def setUp(self):
        self.ps = PersistentStack()

    def test_append(self):
        current = []
        TRIALS = 100
        for i in range(TRIALS):
            x = random.randint(1, 100)
            self.ps.append(x)
            current.append(x)
            self.assertEqual(self.ps.peek(), current[-1])
            self.assertEqual(self.ps.current_version, current)
            self.assertEqual(self.ps.current_version_number, i+1)

    def test_pop(self):
        current = []
        TRIALS = 100
        for _ in range(TRIALS):
            x = random.randint(1, 100)
            self.ps.append(x)
            current.append(x)
        for _ in range(TRIALS):
            self.assertEqual(self.ps.pop(), current.pop())

    def test_alternate(self):
        history = []
        current = [1, 2, 3]
        history.append(current)
        ps = PersistentStack(current)

        TRIALS = 100
        for i in range(TRIALS):
            if i % 2 == 0:
                x = random.randint(1, 100)
                ps.append(x)
                current = current.copy()
                current.append(x)
                history.append(current)
            else:
                ps.pop()
                current = current.copy()
                current.pop()
                history.append(current)

        for i in range(TRIALS):
            self.assertEqual(ps.peek(i), history[i][-1])

    def test_exceptions(self):
        with self.assertRaises(IndexError):
            self.ps.pop()
            self.peek()
            self.ps[10]

        with self.assertRaises(TypeError):
            self.ps['hi']


if __name__ == '__main__':
    unittest.main()
