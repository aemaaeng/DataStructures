class Heap:
    def __init__(self, L=[]):
        self.A = L
        self.make_heap()  # make_heap 함수 호출
    
    def __str__(self):
        return str(self.A)
    
    def __len__(self):
        return len(self.A)

    # 힙 성질을 만족하지 않을 수도 있음
    def heapify_down(self, k, n):
        # k = 옮길 노드 번호, n = heap의 노드 수
        # A[k]가 힙 성질을 만족하지 않으면 밑으로. 힙 성질을 만족하는 위치 찾기
        while 2*k + 1 < n:
            L, R = 2*k + 1, 2*k + 2
            # m = 트리의 세 노드 중 최댓값을 갖는 인덱스, 부모/왼쪽/오른쪽 노드 중 최댓값 찾아 저장
            if L < n and self.A[L] > self.A[k]:
                m = L
            else:
                m = k
            if R < n and self.A[R] > self.A[m]:
                m = R
            # k와 m 비교하기
            if m != k:
                self.A[k], self.A[m] = self.A[m], self.A[k]
                k = m
            else:
                break
    
    def make_heap(self):
        n = len(self.A)
        for k in range(n-1, -1, -1):
            self.heapify_down(k, n)
    
    def heap_sort(self):
        n = len(self.A)
        for k in range(len(self.A) - 1, -1, -1):  # 맨 끝 노드부터 거꾸로 한 칸씩
            self.A[k], self.A[0] = self.A[0], self.A[k]
            n = n - 1
            self.heapify_down(0, n)
            
    def find_max(self):
        if len(self.A) == 0: 
            return None
        return self.A[0]
    
    def heapify_up(self, k):
        while k > 0 and self.A[(k - 1)//2] < self.A[k]:  # 부모 노드가 자식 노드보다 작을 때
            self.A[(k - 1)//2], self.A[k] = self.A[k], self.A[(k - 1)//2]
            k = (k - 1)//2
    
    def insert(self, key):
        self.A.append(key)  # 맨 끝에 값이 삽입됨
        self.heapify_up(len(self.A) - 1)  # 힙이 되도록 맨 끝 노드에서 업 수행
        
    def delete_max(self):
        if len(self.A) == 0:
            return None
        key = self.A[0]  # 최댓값을 key에 저장해둠
        self.A[0], self.A[len(self.A) - 1] = self.A[len(self.A) - 1], self.A[0] #swap
        self.A.pop()
        self.heapify_down(0, len(self.A))  #0번째 노드를 성질에 맞게 재배치
        return key
