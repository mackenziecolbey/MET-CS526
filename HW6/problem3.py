##homework 6 problem 3 Median

import ast
import sys
from problem2 import MinHeap


class MaxHeap(MinHeap):

    def _bubble_up(self, node):
        while node.parent is not None:
            if node.value > node.parent.value:
                node.value, node.parent.value = (
                    node.parent.value, node.value
                )
                node = node.parent
            else:
                break

    def _bubble_down(self, node):
        while node is not None:
            largest = node

            if (node.left is not None and
                    node.left.value > largest.value):
                largest = node.left

            if (node.right is not None and
                    node.right.value > largest.value):
                largest = node.right

            if largest != node:
                node.value, largest.value = (
                    largest.value, node.value
                )
                node = largest
            else:
                break

    def extract_max(self):
        return self.extract_min()


def running_median(values):
    lower_half = MaxHeap()
    upper_half = MinHeap()

    medians = []

    for value in values:

        if lower_half.is_empty() or value <= lower_half.peek():
            lower_half.insert(value)
        else:
            upper_half.insert(value)

        if len(lower_half) > len(upper_half) + 1:
            upper_half.insert(lower_half.extract_max())

        elif len(upper_half) > len(lower_half):
            lower_half.insert(upper_half.extract_min())

        if len(lower_half) == len(upper_half):
            median = (
                lower_half.peek() + upper_half.peek()
            ) / 2
        else:
            median = float(lower_half.peek())

        medians.append(median)

    return medians


values = ast.literal_eval(sys.stdin.read().strip())

print(running_median(values))

