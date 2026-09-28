# MET-CS526 HW2

Problem 1: What is the advantage of using a tail pointer in a linked list?

A tail pointer keeps track of the last node in a linked list. This allows a new node to be added directly to the end of the list without passing through the entire list. Therefore, adding a new node to the end of the list takes O(1) time. 

Problem 2:
  a) What are the base cases of your function, and why? (What should
    ways(0) be?
The base cases are ways(0) = 1 and ways(n) = 0 when n<0. Ways(0) should be 1 because there's one way to climb 0 steps. That is to take no steps. This lets the recursive function to count a way when it reaches 0. If n is negative, ways(n) should be 1 because you can't climb a negative number of steps. These base cases also give the recursive function a point where it stops. 

  b) If you could only climb 1 or 2 steps at a time, what well-known
    sequence would ways(n) produce?
If you could only climb 1 or 2 steps at a time, ways(n) would produce the Fibonacci sequence because each number is found when you add the two numbers before it. 



