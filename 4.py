class Stack:
    def __init__(self):
    self._stack=[]

    def push(self, item):
    self._stack.append(item)

    def pop(self):
    if self.is_empty():
        raise empty('Stack is empty')
    return self_.pop()

    def is_empty(self):
        return len(self._stack) =- 0