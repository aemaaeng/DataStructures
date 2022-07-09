class deque():
    def __init__(self, s):
        self.items = list(s)

    def append(self, c):
        self.items.append(c)

    def appendleft(self, c):
        self.items.insert(0, c)

    def pop(self):
        return self.items.pop()

    def popleft(self):
        return self.items.pop(0)

    def __len__(self):
        return len(self.items)

    def right(self):
        return self.items[-1]

    def left(self):
        return self.items[0]
    