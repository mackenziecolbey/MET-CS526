# MET-CS526 HW2

Introduction
Homework 2 covers linked lists and recursion. Problem 1 explains the advantage of using tail pointer. Problem 2 applies a singly linked list and a driver to test it. Problem 3 uses recursion to find the number of ways to climb stairs. Problem 4 applies a sorted doubly linked list and a driver to test it.

Algorithm
Problem 1: A tail pointer keeps track of the last node in the list. This allows a new node to be added directly to the end of the list without passing through the entire list. Therefore, adding a new node to the end of the list takes O(1) time. 
Problem 2: a) The base cases are ways(0) = 1 and ways(n) = 0 when n<0. Ways(0) should be 1 because there's one way to climb 0 steps. That is to take no steps. This lets the recursive function to count a way when it reaches 0. If n is negative, ways(n) should be 1 because you can't climb a negative number of steps. These base cases also give the recursive function a point where it stops. b) If you could only climb 1 or 2 steps at a time, ways(n) would produce the Fibonacci sequence because each number is found when you add the two numbers before it. 
Problem 3: The ways function uses recursion. For each value of n, it calls itself with n-1, n-2, n-3. The base cases stop the recursion when n reaches 0 or becomes negative.
Problem 4: The doubly linked list keeps a head and a tail. Each node has a value, prev and next. When you add a value, its placed in the correct sorted position. Recursive helper functions are used for total, count, exist, and print_list.

Interesting Aspects
Problem 1: the tail pointer avoids having to go through the list when adding to the end. Problem 2: the list keeps count of its nodes, this makes getting the length easier and simpler. Problem 3: ways(0) returns 1 because there's one way to climb 0 steps, which is taking no steps. Negative values return 0 because you cant count negative steps, that invalid path is not counted. If only 1 or 2 steps are taken at a time, the result follows the Fibonacci sequence. Problem 4: The list stays sorted automatically when you add values. Negative, duplicate, and decimal values are supported. 

How to Run
Problem 1: N/A. 
Problem 2: in the terminal i wrote: python3 problem2_driver < problem2_resources/problem2_basic.txt. The other problem 2 resource test files are run using the same thing but replacing the test file name. 
Problem 3: python3 problem3.py
Problem 4: I wrote python3 problem4_driver.py < problem4_resources/problem4_basic.txt in the terminal. The other problem 4 resources test files can be run by replacing the test file name. 



