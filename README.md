# MET-CS526
Homework 4

Introduction: The assignment covers tree traversals (generic and binary tree), finding the smallest number of elements needed to reach a target, and counting right triangles from a set of points.

Problem 1: General tree
a) preorder traversal: A, B, E, H, F, I, C, D, G. The preorder visits the parental node first, then by its children from left to right.
b) breadth-first traversal: A, B, C, D, E, F, G, H, I. It visits the nodes level by level, from left to right.
c) post tree traversal: H, E, I, F, B, C, G, D, A. It visits the children before their parents, processing each subtree from left to right.
Problem 1: Binary tree
a) in-order traversal: D, G, B, E, A, C, H, F, I. It visits the left subtree first, then parent node, then the right subtree. 

Problem 2: Algorithm: The program reads the target value and numbers. It sorts the numbers from largest to smallest and adds them until the total is greater than the target. It then outputs the number of elements used. How to run: I ran the program with one of the provided input files; Get-Content fewest_1.txt | python smallestNumber.py. Example: input file is fewest_1.txt and the output is input: 3,1,8,2,4,6,9,5 Target: 17 Answer: 3.

Problem 3: Algorithm: The program checks each point as a possible right angle. It calculates the directions to the other points and counts pairs of perpendicular directions. The pairs form right angles. How to run: Run the program with one of the input files provided; Get-Content rightangles_1.txt | python rightTriangles.py. Example: input file is rightangles_1.txt, output is The number of right triangles is: 4. 

Interesting: I found it interesting that perpendicular directions can be used to count right triangles without checking every group possible of three points. 

