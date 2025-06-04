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

    # finction to check if the stack is full 
    def is_full(self): 
        return self.top + 1 == self.capacity
            
    # function to check if the stack is empty
    def is_empty(self): 
        return self.top == -1
    
    # function to look at the element on top of the stack
    def peep(self): 
        return self.array[self.top]

    # funtion to count the number of elements on the stack
    def count(self): 
        return self.top + 1
    
    # function to get the element at the ith position
    def peek(self, index): 
        if self.top == -1: 
            print("stack is empty, cannot peek")
            return 

        if self.top < index: 
            print("stack index out of range, cannot peek")
            return 
        
        return self.array[index]
    # function to change the element at position i
    def change(self, index, element): 
        if self.is_empty(): 
            print("stack is empty, no element to change!")
            return 
        
        if self.top > index: 
            print("stack index out of range, cannot change")
            return 
        
        return self.array[index]
    

# let's test the stack 
stack = Stack(capacity=5)
stack.push(55)
stack.push(66)
stack.push(89)
stack.push(15)
stack.change(1, 99) # change the element at the 1th position (96 before)
stack.pop()
print(f"is the stack empty?: {stack.is_empty()}")
print(f"is the stack full?: {stack.is_full()}")
# element on top of the stack

print(f"element on top of the stack: {stack.peep()}")
print(f"element at position 2: {stack.peek(index=2)}")
print(f"the number of elements on the stack: {stack.count()}")




stack.display_elements()