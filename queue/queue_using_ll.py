class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class Queue:
    
    def __init__(self,capacity):
        self.front = self.rear = -1
        
    def enQueue(self,data):
        if self.front == self.rear != -1:
            raise ValueError("")
    
    def isEmpty(self):
        return self.front == None

    def deQueue(self):
        if self.isEmpty():
            raise ValueError("Can not dequeue more items")
        self.front = self.front.next
        pass


if __name__ == "__main__":
    queue = Queue()
    
