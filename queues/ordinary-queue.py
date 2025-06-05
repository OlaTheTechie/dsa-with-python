"""
implementing the simple queue data structure in python
"""

class Queue: 
    def __init__(self, capacity): 
        self.capacity = capacity
        self.arr = [0 for i in range(self.capacity)]
        self.rear = -1
        self.front = -1
        self.count = 0
    
    def is_empty(self): 
        return self.count == 0
    
    def is_full(self): 
        return self.count == self.capacity
    
    def enque(self, element): 
        if self.is_empty(): 
            self.rear += 1
            self.front += 1
            self.arr[self.front] = element
            self.count += 1

            return 
        if self.is_full(): 
            print("queue is full, cannot enqueue")
            return
        
        self.rear += 1
        self.count += 1
        self.arr[self.rear] = element

        return 
    
    def dequeue(self): 
        if self.is_empty(): 
            print("queue is empty, no element to dequeue")
            return 
        
        self.arr[self.front] = 0
        self.front += 1
        self.count -= 1
        return
    

    def display_items(self): 
        if self.is_empty(): 
            print("queue is empty, no item to display!")
            return 
        
        print("Below are the elements of the queue: ")
        
        for item in self.arr[self.front: self.rear + 1]: 
            
            print(item)
        return 
    
    def get_count(self): 
        return self.count
    


# now lets test our queue

queue = Queue(capacity=5)
queue.enque(88)
queue.enque(89)
queue.enque(90)
queue.dequeue()
queue.display_items()
print(f"n of elements in the queue: {queue.get_count()}")
