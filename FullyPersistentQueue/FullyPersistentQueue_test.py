import unittest
import random
from FullyPersistentQueue import FullyPersistentQueue
from FullyPersistentQueue import Node


class TestFullyPersistentQueueMethods(unittest.TestCase):

    # Testing linked list subroutines.

    # Linked list to a list.
    def to_list(head):
        res = []
        while head is not None:
            res.append(head.val)
            head = head.next
        return res

    # Array to linked list.
    def to_linked_list(nums):
        if len(nums) == 0:
            return None
        head = Node(nums[0])
        current = head
        for x in nums[1:]:
            new = Node(x)
            current.next = new
            current = new
        return head

    def get_tail(head):
        prev = None
        while head is not None:
            prev = head
            head = head.next
        return prev

    def test_reverse(self):
        tests = [[], [1], [1, 2], [1, 2, 3]]
        for test in tests:
            head = TestFullyPersistentQueueMethods.to_linked_list(test)
            rev = TestFullyPersistentQueueMethods.to_list(head)
            rev.reverse()

            rev_head = FullyPersistentQueue._reverse(head)
            self.assertEqual(rev,
                             TestFullyPersistentQueueMethods.to_list(rev_head))

    def test_reverse_empty(self):
        self.assertEqual(TestFullyPersistentQueueMethods.to_list(None), [])

    def test_reverse_singleton(self):
        head = Node(1)
        self.assertEqual(TestFullyPersistentQueueMethods.to_list(head), [1])

    # Testing the queue.
    def queue_to_list(q):
        f = TestFullyPersistentQueueMethods.to_list(q.F)
        r = TestFullyPersistentQueueMethods.to_list(q.R)
        return r + f[::-1]

    def test_init_peek(self):
        q = FullyPersistentQueue([1, 2])
        self.assertEqual(q.peek(), 1)

    def test_init_enqueue(self):
        q = FullyPersistentQueue([1, 2, 3])
        v = q.enqueue(4)
        # self.assertEqual(q.peek(), 1)
        self.assertEqual(v.peek(), 1)

    def test_init_dequeue(self):
        q = FullyPersistentQueue([1, 2])
        self.assertEqual(q.F.val, 2)
        self.assertEqual(q.F.next.val, 1)
        assert q.R is None

        val1, q1 = q.dequeue()
        val2, q2 = q1.dequeue()
        self.assertEqual(val1, 1)
        self.assertEqual(val2, 2)
        with self.assertRaises(IndexError):
            q2.dequeue()

    def test_F(self):
        q1 = FullyPersistentQueue([1])
        self.assertEqual(q1.F.val, 1)
        q2 = q1.enqueue(2)
        self.assertEqual(q2.F.val, 2)
        self.assertEqual(q2.F.next.val, 1)

        val, q = q2.dequeue()
        self.assertEqual(val, 1)

    def test_to_list1(self):
        init = [1, 2]
        q_init = FullyPersistentQueue(init)
        self.assertEqual(
            TestFullyPersistentQueueMethods.queue_to_list(q_init), init)

    def test_to_list2(self):
        q_init = FullyPersistentQueue([1, 2, 3])
        self.assertEqual(
            TestFullyPersistentQueueMethods.queue_to_list(q_init), [1, 2, 3])

        q = q_init.enqueue(4)
        self.assertEqual(
            TestFullyPersistentQueueMethods.queue_to_list(q), [1, 2, 3, 4])

        _, q = q.dequeue()
        self.assertEqual(
            TestFullyPersistentQueueMethods.queue_to_list(q), [2, 3, 4])

    def test_empty(self):
        q = FullyPersistentQueue()
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_random(self):
        q_current = [1, 2, 3]
        q = FullyPersistentQueue(q_current)
        lists = [q_current]
        queues = [q]

        TRIALS = 100
        # Enqueue
        for _ in range(TRIALS):
            x = random.randint(-100, 100)
            current_queue = random.choice(queues)
            current_list = TestFullyPersistentQueueMethods.queue_to_list(
                current_queue)
            current_list.append(x)
            lists.append(current_list)
            queues.append(current_queue.enqueue(x))

        # Dequeue
        for _ in range(TRIALS):
            current_queue = random.choice(queues)
            current_list = TestFullyPersistentQueueMethods.queue_to_list(
                current_queue)
            if len(current_list) > 0:
                current_list = current_list[1:]
                _, new = current_queue.dequeue()
                lists.append(current_list)
                queues.append(new)

        for list, q in zip(lists, queues):
            self.assertEqual(
                list, TestFullyPersistentQueueMethods.queue_to_list(q))


if __name__ == '__main__':
    unittest.main()
