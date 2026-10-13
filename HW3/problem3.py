
# Stack using an array

class ArrayStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def reverse(self):
        if self.is_empty():
            return
        item = self.pop()
        self.reverse()
        insert_bottom(self, item)


def insert_bottom(stack, item):
    if stack.is_empty():
        stack.push(item)
        return
    top = stack.pop()
    insert_bottom(stack, item)
    stack.push(top)


# Stack using a singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedStack:
    def __init__(self):
        self.top = None

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            return None
        item = self.top.data
        self.top = self.top.next
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def reverse(self):
        if self.is_empty():
            return
        item = self.pop()
        self.reverse()
        insert_bottom_linked(self, item)


def insert_bottom_linked(stack, item):
    if stack.is_empty():
        stack.push(item)
        return
    top = stack.pop()
    insert_bottom_linked(stack, item)
    stack.push(top)


# Stack using a doubly linked list

class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedStack:
    def __init__(self):
        self.top = None

    def push(self, item):
        node = DoubleNode(item)
        node.next = self.top
        if self.top is not None:
            self.top.prev = node
        self.top = node

    def pop(self):
        if self.is_empty():
            return None
        item = self.top.data
        self.top = self.top.next
        if self.top is not None:
            self.top.prev = None
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def reverse(self):
        if self.is_empty():
            return
        item = self.pop()
        self.reverse()
        insert_bottom_doubly(self, item)


def insert_bottom_doubly(stack, item):
    if stack.is_empty():
        stack.push(item)
        return
    top = stack.pop()
    insert_bottom_doubly(stack, item)
    stack.push(top)


# Print the stack from bottom to top

def print_array(stack):
    print(", ".join(str(item) for item in stack.items))


def print_linked(stack):
    items = []

    def collect(node):
        if node is None:
            return
        collect(node.next)
        items.append(str(node.data))

    collect(stack.top)
    print(", ".join(items))


# Test the three stacks

array_stack = ArrayStack()
singly_stack = SinglyLinkedStack()
doubly_stack = DoublyLinkedStack()

for number in range(1, 11):
    array_stack.push(number)
    singly_stack.push(number)
    doubly_stack.push(number)

print("Array Stack")
print("Before:", end=" ")
print_array(array_stack)
array_stack.reverse()
print("After:", end=" ")
print_array(array_stack)

print("Singly Linked Stack")
print("Before:", end=" ")
print_linked(singly_stack)
singly_stack.reverse()
print("After:", end=" ")
print_linked(singly_stack)

print("Doubly Linked Stack")
print("Before:", end=" ")
print_linked(doubly_stack)
doubly_stack.reverse()
print("After:", end=" ")
print_linked(doubly_stack)
