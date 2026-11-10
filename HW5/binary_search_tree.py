##homework 5
##binary search tree
#problem 1

import random


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def AddNode(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.add(self.root, value)

    def add(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self.add(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self.add(current.right, value)

    def FindNode(self, value):
        current = self.root

        while current is not None:
            if current.value == value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return False

    def DeleteNode(self, value):
        self.root = self.delete(self.root, value)

    def delete(self, current, value):
        if current is None:
            return None

        if value < current.value:
            current.left = self.delete(current.left, value)
        elif value > current.value:
            current.right = self.delete(current.right, value)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            smallest = current.right
            while smallest.left is not None:
                smallest = smallest.left

            current.value = smallest.value
            current.right = self.delete(current.right, smallest.value)

        return current

    def PrintTree(self):
        self.print_tree(self.root)
        print()

    def print_tree(self, current):
        if current is not None:
            self.print_tree(current.left)
            print(current.value, end=" ")
            self.print_tree(current.right)


numbers = random.sample(range(1, 1001), random.randint(5, 50))

print("Input Set:")
print(numbers)

tree = BST()

for number in numbers:
    tree.AddNode(number)

print("\nInitial Tree:")
tree.PrintTree()

new_number = random.randint(1, 1000)

while tree.FindNode(new_number):
    new_number = random.randint(1, 1000)

print("\nAdding Node:", new_number)
tree.AddNode(new_number)
tree.PrintTree()

delete_number = random.choice(numbers)

print("\nDeleting Node:", delete_number)
tree.DeleteNode(delete_number)
tree.PrintTree()

find_number = random.choice(numbers)

print("\nSearching for:", find_number)
if tree.FindNode(find_number):
    print("Node found.")
else:
    print("Node not found.")

missing_number = 0

print("\nSearching for:", missing_number)
if tree.FindNode(missing_number):
    print("Node found.")
else:
    print("Node not found.")

