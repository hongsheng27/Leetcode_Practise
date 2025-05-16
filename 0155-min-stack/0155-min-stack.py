class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val):
        self.stack.append(val)
        if not self.min:
            self.min.append(val)
        else:
            self.min.append(min(self.min[-1], val))


    def pop(self):
        self.stack.pop()
        self.min.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()