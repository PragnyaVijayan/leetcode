# Design a class that supports pop, push, peek, getMin

class MinStack:
    def __init__(self):
        self.stack = [] # Blue
        self.min_stack = [] # Green
        
    def pop(self):
        if self.stack:
            self.stack.pop()
        if self.min_stack:
            self.min_stack.pop()
        
    def push(self, n):
        self.stack.append(n)
        if self.min_stack:
            if n < self.min_stack[-1]:
                self.min_stack.append(n)
            else:
                self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(n)
    
    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1
        
    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return -1

def main():
    my_stack = MinStack()
    
    my_stack.push(3)
    my_stack.push(4)
    my_stack.push(8)
    my_stack.push(6)
    my_stack.push(3)
    my_stack.push(-3)
    my_stack.push(45)
    
    print(my_stack.getMin())

if __name__ == "__main__":
    main()
