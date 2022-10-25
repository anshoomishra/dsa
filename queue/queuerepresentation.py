# Array Implementation
class Queue:
    def __init__(self,capacity) -> None:
        self.capacity = capacity
        self.front = -1
        self.rear = -1
        self.queue = [None]*capacity

    def enqueue(self,data):
        pass

    def dequeue(self):
        pass

    def is_empty(self):
        pass

    def is_full(self):
        pass
    

if __name__ == "__main__":
    queue = Queue(10)