class Queue:
    def __init__(self, n):
        self.size = n # 전체 크기
        self.itmes = [None] * n # 각 아이템
        self.rear = -1 # rear
        self.front = -1 # front

    def enQueue(self, item):
        if self.isFull():
            print('isFull')
        else:
            self.rear += (self.rear + 1) % self.size
            self.itmes[self.rear] = item

    def deQueue(self):
        if self.isEmpty():
            print('isEmpty')
        else:
            self.front += 1
            item = self.itmes[self.front]
            self.itmes[self.front] = None
            return item

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.rear == (self.rear + 1) % self.size

    def Peek(self):
        return self.itmes[self.front]

q = Queue(4)
print(q.itmes)
q.enQueue('A')
q.enQueue('B')
print(q.itmes)
print(q.rear)
print(q.front)
print(q.isEmpty())
print(q.deQueue())
print(q.itmes)
print(q.front)
print(q.deQueue())
print(q.isEmpty())
print(q.itmes)
q.enQueue('C')
q.enQueue('D')
print(q.itmes)
print(q.deQueue())
print(q.deQueue())
print(q.itmes)
print(q.isEmpty())
print(q.isFull())