import unittest
import random
from PersistentList import PersistentList


class TestPersistentListMethods(unittest.TestCase):

    def setUp(self):
        self.pl = PersistentList()

    def test_append(self):
        current = []
        TRIALS = 100
        for i in range(TRIALS):
            x = random.randint(1, 100)
            self.pl.append(x)
            current.append(x)
            self.assertEqual(self.pl.get(), current)
            self.assertEqual(self.pl.current_version, current)
            self.assertEqual(self.pl.current_version_number, i+1)

    def test_pop(self):
        current = []
        TRIALS = 100
        for _ in range(TRIALS):
            x = random.randint(1, 100)
            self.pl.append(x)
            current.append(x)
        for _ in range(TRIALS):
            self.assertEqual(self.pl.pop(), current.pop())

    def test_alternate(self):
        history = []
        current = [1, 2, 3]
        history.append(current)
        pl = PersistentList(current)

        TRIALS = 100
        for i in range(TRIALS):
            if i % 2 == 0:
                x = random.randint(1, 100)
                pl.append(x)
                current = current.copy()
                current.append(x)
                history.append(current)
            else:
                pl.pop()
                current = current.copy()
                current.pop()
                history.append(current)

        for i in range(TRIALS):
            self.assertEqual(pl.get(i), history[i])

    def test_set_del(self):
        history = []
        current = [1, 2, 3]
        history.append(current)
        pl = PersistentList(current)

        TRIALS = 100
        for _ in range(TRIALS):
            x = random.randint(1, 100)
            pl[2] = x
            current = current.copy()
            current[2] = x
            history.append(current)

        for i in range(TRIALS):
            self.assertEqual(pl.get(i), history[i])

        del pl[2]
        del current[2]
        self.assertEqual(pl.current_version, current)

    def test_exceptions(self):
        self.pl.append(2)
        with self.assertRaises(IndexError):
            self.pl[10]
            del self.pl[10]
            self.pl.get(10)
            self.pl.get(0).pop()

        with self.assertRaises(TypeError):
            self.pl['hi']
            self.pl.get('hi')


if __name__ == '__main__':
    unittest.main()
