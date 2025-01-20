class Stack:
    def __init__(self):
        self.item = []

    def push(self, item):
         self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("A pilha está vazia")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)