# Last updated: 6/19/2025, 11:46:32 AM
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
    
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1
        
    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return -1
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()