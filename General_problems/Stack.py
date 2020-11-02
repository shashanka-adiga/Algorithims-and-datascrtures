class Stack:
    def __init__(self, max_size):
        self.stack = [None]*max_size
        self.curr = -1
        self.size = max_size

    def push(self,  data):
        if self.curr < self.size -1:
            self.curr += 1
            self.stack[self.curr] = data
        else:
            print("stack overflow!")

    def pop(self):
        if self.curr > -1:
            self.stack[self.curr] = None
            self.curr = self.curr - 1
        else:
            print("stack underflow!")

    def print_stack(self):
        if self.curr > -1:
            print(self.stack)

stack = Stack(3)
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.push(3)
stack.push(4)
stack.print_stack()
