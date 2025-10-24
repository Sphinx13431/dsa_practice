'''
Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time
'''
class MinStack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, value: int):
        if self.isEmpty():
            self.stack.append([value, value])
        else:
            curr_mini = min(value, self.stack[self.top][1])
            self.stack.append([value, curr_mini])
        self.top += 1

    def pop(self) -> int:
        if self.isEmpty():
            print("The stack is empty")
            return -1
        dele = self.stack.pop()
        self.top -= 1
        return dele[0]  # return the value, not the min

    def getMin(self) -> int:
        if self.isEmpty():
            print("The stack is empty")
            return -1
        return self.stack[self.top][1]

    def isEmpty(self) -> bool:
        return self.top == -1
