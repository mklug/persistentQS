# Partially persistent stack.
# Only inspecting operation is peek.
# Only the update operations (append, pop) modify the version number.

class PersistentStack:

    def __init__(self, nums=None):
        self.version_peek = [nums[-1]] if nums is not None else [None]
        self.current_version_number = 0
        self.current_version = nums.copy() if nums is not None else []

    def append(self, item):
        self.version_peek.append(item)
        self.current_version.append(item)
        self.current_version_number += 1

    def pop(self):
        if len(self.current_version) == 0:
            raise IndexError("Pop from an empty list")
        res = self.current_version.pop()
        if len(self.current_version) > 0:
            self.version_peek.append(self.current_version[-1])
        else:
            self.version_peek.append(None)
        # self.version_peek.append(res)
        self.current_version_number += 1
        return res

    def version_number(self):
        return self.current_version_number

    def peek(self, version_number=None):
        if version_number is None:
            version_number = self.current_version_number
        if type(version_number) != int:
            raise TypeError("Version number must be an integer")
        if version_number < 0 or version_number > self.current_version_number:
            raise IndexError("Invalid version number")
        if self.version_peek[version_number] is None:
            raise IndexError("Peeking in empty stack")
        return self.version_peek[version_number]

    def __getitem__(self, index):
        if type(index) != int:
            raise TypeError("Version number must be an integer")
        return self.current_version[index]

    def __len__(self):
        return len(self.current_version)

    def __iter__(self):
        yield from self.current_version

    def __reversed__(self):
        return reversed(self.current_version)

    def __repr__(self):
        return f'{self.__module__}({self.current_version})'
