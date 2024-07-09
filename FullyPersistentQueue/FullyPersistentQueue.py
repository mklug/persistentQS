class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# Two lists: Forward and Reverse (F and R).


class FullyPersistentQueue:

    def __init__(self, nums=None):
        if nums is None:
            self.F = None
            self._peek = None
            self.len = 0
        else:
            current = Node(nums[0])
            for x in nums[1:]:
                new = Node(x, current)
                current = new
            self.F = current
            self._peek = nums[0]
            self.len = len(nums)

        self.R = None

    def enqueue(self, item):
        new = FullyPersistentQueue([item])
        new.F.next = self.F
        new.R = self.R
        new._peek = self._peek
        new.len = self.len + 1
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
        if self.len == 0:
            raise IndexError("Dequeue from an empty queue")
        if self.R is None:
            self._reset()
        res_val = self.R.val
        res_queue = FullyPersistentQueue()
        res_queue.R = self.R.next
        res_queue.F = self.F

        if res_queue.R is not None:
            res_queue._peek = res_queue.R.val
        elif res_queue.F is not None:
            res_queue._reset
            res_queue._peek = res_queue.R.val
        else:
            res_queue._peek = None

        res_queue.len = self.len - 1
        return res_val, res_queue

    def peek(self):
        if self.len == 0:
            raise IndexError("Peeking at an empty queue")
        return self._peek

    def __len__(self):
        return len(self.len)

    def __iter__(self):
        self._reverse
        head = self.R
        while head is not None:
            yield head.val
            head = head.next

    def __repr__(self):
        return f'{self.__module__}(next={self._peek})'
