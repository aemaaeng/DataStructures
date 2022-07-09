class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, val):
        self.items.append(val)
    def dequeue(self):
        try:
            return self.items.pop(0)
        except IndexError:
            print("Queue is Empty")
    def front(self):
        try:
            return self.items[0]
        except:
            print("Queue is Empty")
    def __len__(self):
        return len(self.items)
    def isEmpty(self):
        return len(self)