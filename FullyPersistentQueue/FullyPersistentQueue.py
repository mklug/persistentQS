class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# Two lists: Forward and Reverse (F and R).


class FullyPersistentQueue:

    def __init__(self, nums=None):
        if nums is None:
            self.F = None
            self.tuple = ()
        else:
            current = Node(nums[0])
            for x in nums[1:]:
                new = Node(x, current)
                current = new
            self.F = current
            self.tuple = tuple(nums)

        self.R = None

    def enqueue(self, item):
        new = FullyPersistentQueue([item])
        new.F.next = self.F
        new.R = self.R
        new.tuple = self.tuple + (item,)
        return new

    # Creates a reverse of the linked list and returns
    # the head.
    def _reverse(head):
        prev = None
        while head:
            new = Node(head.val, prev)
            prev = new
            head = head.next
        return prev

    # Possibly linear time operation.
    def _reset(self):
        self.R = FullyPersistentQueue._reverse(self.F)
        self.F = None

    def dequeue(self):
        if len(self.tuple) == 0:
            raise IndexError("Dequeue from an empty queue")
        if self.R is None:
            self._reset()
        res_val = self.R.val
        res_queue = FullyPersistentQueue()
        res_queue.R = self.R.next
        res_queue.F = self.F
        res_queue.tuple = self.tuple[1:]
        return res_val, res_queue

    def peek(self):
        if len(self.tuple) == 0:
            raise IndexError("Peeking at an empty queue")
        return self.tuple[0]

    def to_list(self):
        return list(self.tuple)

    def __len__(self):
        return len(self.tuple)

    def __iter__(self):
        yield from self.tuple

    def __reversed__(self):
        return reversed(self.tuple)

    def __repr__(self):
        return f'{self.__module__}(next={self.peek()})'
