class PersistentList:

    def __init__(self, nums=None):
        self.versions = [nums.copy()] if nums is not None else [[]]
        self.current_version_number = 0
        self.current_version = self.versions[self.current_version_number]

    def update(self, new_version):
        if type(new_version) != list:
            raise TypeError("New version must be a list")
        self.versions.append(new_version)
        self.current_version_number += 1
        self.current_version = self.versions[self.current_version_number]

    def append(self, item):
        new_version = self.current_version.copy()
        new_version.append(item)
        self.update(new_version)

    def pop(self):
        if len(self.current_version) == 0:
            raise IndexError("Pop from an empty list")
        new_version = self.current_version.copy()
        res = new_version.pop()
        self.update(new_version)
        return res

    def version_number(self):
        return self.current_version_number

    def get(self, version_number=None):
        if version_number is None:
            version_number = self.current_version_number
        if type(version_number) != int:
            raise TypeError("Version number must be an integer")
        if version_number < 0 or version_number > self.current_version_number:
            raise IndexError("Invalid version number")
        return self.versions[version_number]

    def __getitem__(self, index):
        if type(index) != int:
            raise TypeError("Version number must be an integer")
        return self.current_version[index]

    def __setitem__(self, index, value):
        if type(index) != int:
            raise TypeError("Version number must be an integer")
        new_version = self.current_version.copy()
        new_version[index] = value
        self.update(new_version)

    def __delitem__(self, index):
        if type(index) != int:
            raise TypeError("Version number must be an integer")
        new_version = self.current_version.copy()
        del new_version[index]
        self.update(new_version)

    def __len__(self):
        return len(self.current_version)

    def __iter__(self):
        yield from self.current_version

    def __reversed__(self):
        return reversed(self.current_version)

    def __repr__(self):
        return f'{self.__module__}({self.current_version})'
