class Queue:
    def __init__(self, max_size):
        self.queue = [None]*max_size
        self.size = max_size
        self.curr = -1

    def front(self,data):
        if self.curr < self.size -1:
            self.curr += 1
            self.queue[self.curr] = data
        else:
            print("queue overflow!")

    def delete(self):
        if self.curr > -1:
            self.queue[self.curr] = None
            self.curr -= 1
        else:
            print("queue underflow!")

    def print_queue(self):
        if self.curr > -1:
            print(self.queue)
        else:
            print("queue is empty!")

q = Queue(3)
q.front(1)
q.front(2)
q.front(3)
q.delete()
q.front(4)
q.print_queue()