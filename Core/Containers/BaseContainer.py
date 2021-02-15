class BaseContainer:
    def __init__(self):
        self._container = []

    def append(self, *args, **kwargs):
        raise NotImplemented()

    def last(self):
        return self._container[-1]

    def __iter__(self):
        self.idx = -1
        return self

    def __next__(self):
        if self.idx < len(self._container) - 1:
            self.idx += 1
            return self._container[self.idx]
        else:
            raise StopIteration()

    def __repr__(self):
        return f'<{self.__class__.__name__}> len:{len(self)}'

    def __len__(self):
        return len(self._container)

    def __getitem__(self, index: int):
        return self._container[index]

    def __delitem__(self, index: int):
        del self._container[index]
