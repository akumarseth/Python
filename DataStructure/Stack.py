class Stack:

    # Constructor
    def __init__(self):
        self.stack = list()
        self.maxSize = 8
        self.top = 0

    # Adds element to the Stack
    def push(self, data):
        if self.top >= self.maxSize:
            return ("Stack Full!")
        self.stack.append(data)
        self.top += 1
        return True

    # Removes element from the stack
    def pop(self):
        if self.top <= 0:
            return ("Stack Empty!")
        item = self.stack.pop()
        self.top -= 1
        return item

    # Size of the stack
    def size(self):
        return self.top

s = Stack()
print(s.push(1))  # prints True
print(s.push(2))  # prints True
print(s.push(3))  # prints True
print(s.push(4))  # prints True
print(s.push(5))  # prints True
print(s.push(6))  # prints True
print(s.push(7))  # prints True
print(s.push(8))  # prints True
print(s.push(9))  # prints Stack Full!
print(s.size())  # prints 8
print(s.pop())  # prints 8
print(s.pop())  # prints 7
print(s.pop())  # prints 6
print(s.pop())  # prints 5
print(s.pop())  # prints 4
print(s.pop())  # prints 3
print(s.pop())  # prints 2
print(s.pop())  # prints 1
print(s.pop())  # prints Stack Empty!