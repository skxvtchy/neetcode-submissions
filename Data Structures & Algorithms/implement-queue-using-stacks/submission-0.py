class MyQueue:

    def __init__(self):
        self.arr = []
        self.stack = []

    def push(self, x: int) -> None:
        return self.arr.append(x)

    def pop(self) -> int:
        # self.stack = self.arr.pop()
        test = self.arr.pop(0)
        return test
    def peek(self) -> int:
        return self.arr[0]

    def empty(self) -> bool:
        if len(self.arr)>0:
            return False
        return True        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()