class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, value: int):
        self.stack.append(value)
        self.top += 1

    def pop(self):
        if self.isEmpty():
            return -1
        del_ele = self.stack.pop()
        self.top -= 1
        return del_ele

    def peek(self):
        if self.isEmpty():
            return -1
        return self.stack[self.top]

    def isEmpty(self):
        return self.top == -1
