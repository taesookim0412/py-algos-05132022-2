# 19.28% / 21.75%

class MyQueue:

    def __init__(self):
        # Queue in a stack ds
        self.stck = []
        # Reversed Queue
        self.queueStck = []

    def push(self, x: int) -> None:
        while (len(self.queueStck) > 0):
            self.stck.append(self.queueStck.pop())
        self.stck.append(x)

    def pop(self) -> int:
        while (len(self.stck) > 0):
            self.queueStck.append(self.stck.pop())
        if self.queueStck:
            return self.queueStck.pop()
        return -1

    def peek(self) -> int:
        while len(self.stck) > 0:
            self.queueStck.append(self.stck.pop())
        if self.queueStck:
            return self.queueStck[-1]
        return -1

    def empty(self) -> bool:
        return len(self.stck) == 0 and len(self.queueStck) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()