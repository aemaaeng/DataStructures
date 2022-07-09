# find_slot(key) 구현
class HashOpenAddr:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None]*self.size
        self.values = [None]*self.size
    def __str__(self):
        s = ""
        for k in self:
            if k == None:
                t = "{0:5s}|".format("")
            else:
                t = "{0:-5d}|".format(k)
            s = s + t
        return s
    def __iter__(self):
        for i in range(self.size):
            yield self.keys[i]

    def find_slot(self, key):
        i = self.hash_function(key)
        start = i
        while self.keys[i] is not None and self.keys[i] != key:
            i = (i + 1) % self.size
            if i == start:
                return 'FULL'
        return i

    def set(self, key, value=None):  # 삽입연산
        i = self.find_slot(key)
        if i == 'FULL':  # H의 용량을 키움
            # self.size += 1
            return None
        # key 값이 이미 있으면 value 수정
        if self.keys[i] is not None:
            self.values[i] = value
        else:
        # key 값이 없다면 key와 value 추가
            self.keys[i] = key
            self.values[i] = value
        return key

    def hash_function(self, key):
        return key % self.size

    def remove(self, key):  # 위로 올리는게 작동 안 되고 있음!
        i = self.find_slot(key)
        if self.keys[i] is None:
            return None  # key is not in the table
        j = i  # self.keys[j] = 이사해야할 slot
        while True:
            self.keys[i] = None  
            while True:  # 이사할 곳 찾기
                j = (j + 1) % self.size
                if self.keys[j] is None:
                    return key
                k = self.hash_function(self.keys[j])
                if not (k <= j < i or i < k <= j or j < i < k):
                    break
            self.keys[i] = self.keys[j]
            i = j

    def search(self, key):
        i = self.find_slot(key)
        if i == 'FULL':
            return None
        # key 값이 이미 있고 key값과 같으면 key 리턴
        if self.keys[i] is not None and self.keys[i] == key:
            return key
        else:
            return None

    def __getitem__(self, key):
        return self.search(key)
    def __setitem__(self, key, value):
        self.set(key, value)

H = HashOpenAddr()
while True:
    cmd = input().split()
    if cmd[0] == 'set':
        key = H.set(int(cmd[1]))
        if key == None: print("* H is full!")
        else: print("+ {0} is set into H".format(cmd[1]))
    elif cmd[0] == 'search':
        key = H.search(int(cmd[1]))
        if key == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'remove':
        key = H.remove(int(cmd[1]))
        if key == None:
            print("- {0} is not found, so nothing happens".format(cmd[1]))
        else:
            print("- {0} is removed".format(cmd[1]))
    elif cmd[0] == 'print':
        print(H)
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")