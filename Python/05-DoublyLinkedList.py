class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = self
        self.prev = self
    def __str__(self):
        return str(self.key)

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()

    def __iter__(self):
        v = self.head.next
        while v != self.head:
            yield v
        v = v.next

    def __str__(self):
        return " -> ".join(str(v.key) for v in self)

    def printList(self):
        v = self.head.next
        print("h -> ", end="")
        while v != self.head:
            print(str(v.key) + " -> ", end="")
            v = v.next
        print("h")

    def splice(self, a, b, x):  # 세 개의 노드 a, b, x
        if a == None or b == None or x == None:
            return
        #  a부터 b까지 잘라내기
        a.prev.next = b.next
        b.next.prev = a.prev

        # 잘라낸 부분을 x 다음에 넣기
        x.next.prev = b
        b.next = x.next
        a.prev = x
        x.next = a

    def search(self, key):
        v = self.head  # dummy node
        while v.next != self.head:
            if v.key == key:
                return v
            v = v.next
        if v.key == key:
            return v
        return None

    def deleteNode(self, x):
        if x == None or x == self.head:
            return
        x.prev.next, x.next.prev = x.next, x.prev

    def popFront(self):
        if self.head.next == self.head:  # 비어 있는 경우는 제외
            return None
        key = self.head.next.key
        self.deleteNode(self.head.next)
        return key

    def popBack(self):
        if self.head.prev == self.head:
            return None
        key = self.head.prev.key
        self.deleteNode(self.head.prev)
        return key

    def moveAfter(self, a, x):
        L.splice(a, a, x)

    def moveBefore(self, a, x):
        L.splice(a, a, x.prev)

    def insertBefore(self, x, key):
        L.moveBefore(Node(key), x)

    def insertAfter(self, x, key):
        L.moveAfter(Node(key), x)

    def pushFront(self, key):
        L.insertAfter(self.head, key)

    def pushBack(self, key):
        L.insertBefore(self.head, key)

    def isEmpty(self):  # 비어 있으면 True, 아니면 False
        if self.head.prev == self.head:
            return True
        else:
            return False

    def first(self):  # 가장 앞 노드 리턴, 빈 리스트면 None
        if self.head.next == self.head:
            return None
        else:
            return self.head.next

    def last(self):  # 가장 뒷 노드 리턴, 빈 리스트면 None
        if self.head.next == self.head:
            return None
        else:
            return self.head.prev


    #def join(self, list): # 두 리스트 연결하는 함수 (splice 이용)


    #def split(self, x):  # x부터 마지막까지 떼어내 새 리스트 만들어 리턴.


# 이 아래부터는 실습에 필요한 코드임
L = DoublyLinkedList()
while True:
    cmd = input().split()
    if cmd[0] == 'pushF':
        L.pushFront(int(cmd[1]))
        print("+ {0} is pushed at Front".format(cmd[1]))
    elif cmd[0] == 'pushB':
        L.pushBack(int(cmd[1]))
        print("+ {0} is pushed at Back".format(cmd[1]))
    elif cmd[0] == 'popF':
        key = L.popFront()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Front".format(key))
    elif cmd[0] == 'popB':
        key = L.popBack()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Back".format(key))
    elif cmd[0] == 'search':
        v = L.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print("* {0} is found!".format(cmd[1]))
    elif cmd[0] == 'insertA':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertAfter(x, int(cmd[2]))
            print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'insertB':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertBefore(x, int(cmd[2]))
            print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'delete':
        x = L.search(int(cmd[1]))
        if x == None:
            print("- {0} is not found, so nothing happens".format(cmd[1]))
        else:
            L.deleteNode(x)
            print("- {0} is deleted".format(cmd[1]))
    elif cmd[0] == "first":
        print("* {0} is the value at the front".format(L.first()))
    elif cmd[0] == "last":
        print("* {0} is the value at the back".format(L.last()))
    elif cmd[0] == 'print':
        L.printList()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
        