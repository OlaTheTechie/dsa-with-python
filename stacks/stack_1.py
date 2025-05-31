# the simple stack class 

class Stack: 
    def __init__(self, capacity): 
        self.array = []
        self.top = -1
        self.capacity = capacity

    def push(self, element): 
        if (self.top >= self.capacity): 
            print("Stack is full!")
            return
        self.top += 1
        # self.array[self.top] = element
        self.array.append(element)
    
    def pop(self): 
        if (self.top < 0): 
            print("stack is empty, cannot perform a pop")
            return 
        self.array[self.top] = 0
        self.top -= 1

    def display_elements(self): 
        if (self.top < 0): 
            print("stact is empty, nothing to display")
            return 
        for i in self.array[:self.top + 1]: 
            print(i, " ")
            


# let's test the stack 
stack = Stack(capacity=5)
stack.push(55)
stack.push(66)
stack.pop()
stack.display_elements()