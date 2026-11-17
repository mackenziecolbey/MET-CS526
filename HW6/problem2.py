##Homework 6 problem 2 Heap

import ast
import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class MinHeap:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def _get_node(self, position):
        if position < 1 or position > self.size:
            return None

        path = bin(position)[3:]
        current = self.root

        for direction in path:
            if direction == "0":
                current = current.left
            else:
                current = current.right

        return current

    def _bubble_up(self, node):
        while node.parent is not None:
            if node.value < node.parent.value:
                node.value, node.parent.value = (
                    node.parent.value, node.value
                )
                node = node.parent
            else:
                break

    def _bubble_down(self, node):
        while node is not None:
            smallest = node

            if (node.left is not None and
                    node.left.value < smallest.value):
                smallest = node.left

            if (node.right is not None and
                    node.right.value < smallest.value):
                smallest = node.right

            if smallest != node:
                node.value, smallest.value = (
                    smallest.value, node.value
                )
                node = smallest
            else:
                break

    def insert(self, value):
        new_node = Node(value)
        self.size += 1

        if self.root is None:
            self.root = new_node
            return

        parent = self._get_node(self.size // 2)
        new_node.parent = parent

        if self.size % 2 == 0:
            parent.left = new_node
        else:
            parent.right = new_node

        self._bubble_up(new_node)

    def peek(self):
        if self.is_empty():
            raise IndexError("Heap is empty")

        return self.root.value

    def extract_min(self):
        if self.is_empty():
            raise IndexError("Heap is empty")

        minimum = self.root.value

        if self.size == 1:
            self.root = None
            self.size = 0
            return minimum

        last_node = self._get_node(self.size)
        self.root.value = last_node.value

        if self.size % 2 == 0:
            last_node.parent.left = None
        else:
            last_node.parent.right = None

        self.size -= 1
        self._bubble_down(self.root)

        return minimum

    def _find_node(self, node, value):
        if node is None:
            return None

        if node.value == value:
            return node

        found = self._find_node(node.left, value)

        if found is not None:
            return found

        return self._find_node(node.right, value)

    def delete(self, value):
        target = self._find_node(self.root, value)

        if target is None:
            return False

        last_node = self._get_node(self.size)

        if self.size == 1:
            self.root = None
            self.size = 0
            return True

        if target == last_node:
            if self.size % 2 == 0:
                last_node.parent.left = None
            else:
                last_node.parent.right = None

            self.size -= 1
            return True

        target.value = last_node.value

        if self.size % 2 == 0:
            last_node.parent.left = None
        else:
            last_node.parent.right = None

        self.size -= 1

        if (target.parent is not None and
                target.value < target.parent.value):
            self._bubble_up(target)
        else:
            self._bubble_down(target)

        return True

    def build(self, values):
        self.root = None
        self.size = 0

        for value in values:
            self.insert(value)

    def _copy_nodes(self, node, parent=None):
        if node is None:
            return None

        new_node = Node(node.value)
        new_node.parent = parent
        new_node.left = self._copy_nodes(node.left, new_node)
        new_node.right = self._copy_nodes(node.right, new_node)

        return new_node

    def heap_sort(self):
        copy_heap = MinHeap()
        copy_heap.root = self._copy_nodes(self.root)
        copy_heap.size = self.size

        result = []

        while not copy_heap.is_empty():
            result.append(copy_heap.extract_min())

        return result

    def _max_value_width(self, node):
        if node is None:
            return 0

        return max(
            len(str(node.value)),
            self._max_value_width(node.left),
            self._max_value_width(node.right)
        )

    def print_heap(self):
        if self.root is None:
            return

        levels = self.size.bit_length()
        cell_width = max(3, self._max_value_width(self.root) + 1)
        width = (2 ** levels) * cell_width
        height = 2 * levels - 1

        canvas = [
            [" "] * width
            for _ in range(height)
        ]

        def draw(node, depth, index):
            if node is None:
                return

            center = ((2 * index + 1) * width) // (2 ** (depth + 1))
            value = str(node.value)
            start = center - len(value) // 2

            for i, character in enumerate(value):
                canvas[2 * depth][start + i] = character

            if node.left is not None:
                child_center = ((4 * index + 1) * width) // (2 ** (depth + 2))
                connector = (center + child_center) // 2
                canvas[2 * depth + 1][connector] = "/"
                draw(node.left, depth + 1, index * 2)

            if node.right is not None:
                child_center = ((4 * index + 3) * width) // (2 ** (depth + 2))
                connector = (center + child_center) // 2
                canvas[2 * depth + 1][connector] = "\\"
                draw(node.right, depth + 1, index * 2 + 1)

        draw(self.root, 0, 0)

        for row in canvas:
            print("".join(row).rstrip())


if __name__ == "__main__":
    values = ast.literal_eval(sys.stdin.read().strip())

    heap = MinHeap()

    print("Input values:", values)
    print()

    for value in values:
        heap.insert(value)

        print(f"After insert({value}):")
        heap.print_heap()
        print()