class DoubleLinkedList:
    def __init__(self, value):
        self._head = ListItem(value)
        self._length = 1

    def append(self, value):
        curList = self._head
        for i in range(self._length - 1):
            curList = curList.after
        curList.after = ListItem(value)
        curList.after.before = curList
        self._length += 1

    def insert(self, pos, value):
        self._checkpos(pos)
        curList = self._head
        if pos == 0:
            self._head = ListItem(value)
            self._head.after = curList
            curList.before = self._head
        else:
            for i in range(pos):
                curList = curList.after
            temp = ListItem(value)
            curList.before.after = temp
            temp.before = curList.before
            temp.after = curList
            curList.before = temp
        self._length += 1

    def __len__(self):
        return self._length

    def __getitem__(self, pos):
        self._checkpos(pos)
        curList = self._head
        for i in range(pos):
            curList = curList.after
        return curList.value

    def __call__(self):
        _out = list()
        curList = self._head
        for i in range(self._length):
            _out.append(curList.value)
            curList = curList.after
        return _out

    def __repr__(self):
        return str(self.__call__())

    def _checkpos(self, pos):
        if pos < 0 or pos >= self._length:
            raise IndexError('Ensure position is >= 0 and position < length')
        return True

    def drop(self, pos):
        self._checkpos(pos)
        curList = self._head
        if pos == 0:
            self._head = curList.after
            self._head.before = None
        else:
            for i in range(pos):
                curList = curList.after
            curList.before.after = curList.after
            curList.after.before = curList.before
        self._length -= 1
        del curList


class ListItem:
    def __init__(self, value):
        self.value = value
        self.after = None
        self.before = None


if __name__ == '__main__':
    a = DoubleLinkedList('One')
    a.append('Two')
    a.append('Three')
    print(a)
    a.drop(1)
    print(a)
    a.append('Four')
    print(a)
    a.insert(0, 'Five')
    print(a)
    a.insert(2, 'Six')
    print(a)
