class Stack:
    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        if self.stack:
            return self.stack.pop(-1)

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        if self.size():
            return False
        else:
            return True

    def __str__(self):
        return '->'.join(str(c) for c in self.stack[::-1])


# s = Stack()
# s.push(1)
# print(s)
# s.push(2)
# print(s)
# print(s.is_empty())
# s.pop()
# print(s.is_empty())
# s.pop()
# print(s.is_empty())


class MyQueue(object):

    def __init__(self):
        self.stack_actual = Stack()
        self.stack_temp = Stack()

    def push(self, x):
        while not self.stack_actual.is_empty():
            el = self.stack_actual.pop()
            self.stack_temp.push(el)
        self.stack_actual.push(x)
        while not self.stack_temp.is_empty():
            el = self.stack_temp.pop()
            self.stack_actual.push(el)

    def pop(self):
        if not self.stack_actual.is_empty():
            return self.stack_actual.pop()

    def peek(self):
        if not self.stack_actual.is_empty():
            return self.stack_actual.peek()

    def empty(self):
        return self.stack_actual.is_empty()

    def __str__(self):
        return f'{self.stack_actual.size()}: {self.stack_actual.peek()}'


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(1)
# print(obj.peek())
# obj.push(2)
# print(obj.peek())
# obj.push(3)
# print(obj.peek())
# obj.pop()
# print(obj.peek())
