class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
    
    def __str__(self):
        return str(self.key)

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()
    
    def __str__(self):
        return " - ".join(str(k) for k in self)
    
    def preorder(self, v):  # MLR 순
        if v:
            print(v.key, end=" ")
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v):  # LMR 순
        if v:
            self.inorder(v.left)
            print(v.key, end=" ")
            self.inorder(v.right)
                
    def postorder(self, v):  # LRM 순
        if v:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=" ")
    
    def find_loc(self, key):
        if self.size == 0:
            return None
        p = None  # 부모 노드
        v = self.root  # 모험을 떠날 노드
        
        while v != None:
            if v.key == key:
                return v
            elif v.key < key:
                p = v
                v = v.right
            else:
                p = v
                v = v.left
        return p
    
    def search(self, key):
        v = self.find_loc(key)
        if v and v.key == key:
            return v
        else:
            return None
        
    def insert(self, key):
        p = self.find_loc(key)  # O(h)
        if p == None or p.key != key:
            v = Node(key)
            if p == None:
                self.root = v
            else:
                v.parent = p
                if p.key > key:
                    p.left = v
                else:
                    p.right = v
            self.size += 1
            return v
        else:
            return None
    
    def deleteByMerging(self, x):  # deletebyMerging
        a = x.left
        b = x.right
        pt = x.parent
        if a == None:
            c = b
        else:
            c = m = a
            while m.right:
                m = m.right
            m.right = b
            if b:
                b.parent = m
        if self.root == x:
            if c:
                c.parent = None
            self.root = c
        else:
            if pt.left == x:
                pt.left = c
            else:
                pt.right = c
            if c:
                c.parent = pt
        self.size -= 1
    
    def deleteByCopying(self, x):
        pt = x.parent
        L, R = x.left, x.right
        if L:
            y = L
            while y.right:
                y = y.right
            x.key = y.key
            if y.left:
                y.left.parent = y.parent
            if y.parent.left is y:
                y.parent.left = y.left
            else:
                y.parent.right = y.left
            del y
        
        elif not L and R:
            y = R
            while y.left:
                y = y.left
            x.key = y.key
            if y.right:
                y.right.parent = y.parent
            if y.parent.left is y:
                y.parent.left = y.right
            else:
                y.parent.right = y.right
            del y
        
        else:
            if pt == None:
                self.root = None
            else:
                if pt.left is x:
                    pt.left = None
                else:
                    pt.right = None
            del x
            

# 여기서부터는 구름 플랫폼 실습 코드임
T = Tree()

while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        if v != None:
            print("+ {0} is set into H".format(v.key))
        else:
            print(cmd[1], "is already in the tree!")
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'preorder':
        T.preorder(T.root)
        print()
    elif cmd[0] == 'postorder':
        T.postorder(T.root)
        print()
    elif cmd[0] == 'inorder':
        T.inorder(T.root)
        print()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
