class StackNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class FullyPersistentStack:

    def __init__(self, nums=None):
        if nums is None:
            self.root = None
        else:
            self.root = StackNode(val=nums[-1])
            current = self.root
            for x in reversed(nums[:-1]):
                new = StackNode(val=x)
                current.next = new
                current = new

    def append(self, item):
        new = FullyPersistentStack([item])
        new.root.next = self.root
        return new

    def pop(self):
        if self.root == None:
            raise IndexError("Pop from an empty list")
        else:
            res_val = self.root.val
            res_stack = FullyPersistentStack()
            res_stack.root = self.root.next
            return res_val, res_stack

    def peek(self):
        if self.root == None:
            raise IndexError("Peek to an empty list")
        return self.root.val

    def to_list(self):
        current = self.root
        res = []
        while current is not None:
            res.append(current.val)
            current = current.next
        res.reverse()
        return res

    def __len__(self):
        res = 0
        current = self.root
        while current is not None:
            current = current.next
            res += 1
        return res

    def __iter__(self):
        yield from self.to_list()

    def __reversed__(self):
        return reversed(self.to_list())

    def __repr__(self):
        return f'{self.__module__}(top={self.root.val})'
