# MET-CS526

Problem 1: This problem is to merge multiple sorted register logs into one sorted list of sales. Each sale contains a time and a register number. The final list is ordered by time, with lower register numbers coming first when times are equal. The program uses a custom min-heap priority queue to merge the logs efficiently. 

Algorithm: The program reads the register logs and inserts the first sale from each non-empty register into the priority queue. Each time, it removes the sale with the smallest time. If two sales have the same time, the lower register number is selected first. After removing a sale, the program adds the next sale from that same register to the priority queue, if one is available. This continues until all sales have been processed. The priority queue only stores one sale per register at a time, so it never needs more than k entries. Instead of combining and sorting all the sales, the program only compares the next available sale from each register. This makes the merging process more efficient, especially when there are many registers and sales.

How to run: I ran the commands below in the terminal from my HW6 folder. All the results matched the expected outputs in the assignment.

Commands:

Get-Content "Merge Resources/merge_input2.txt" | python problem1.py

Get-Content "Merge Resources/merge_input3.txt" | python problem1.py

Get-Content "Merge Resources/merge_input5.txt" | python problem1.py

Get-Content "Merge Resources/merge_input6.txt" | python problem1.py

Get-Content "Merge Resources/merge_input7.txt" | python problem1.py

Get-Content "Merge Resources/merge_input8.txt" | python problem1.py

Get-Content "Merge Resources/merge_input9.txt" | python problem1.py


Problem 2: The goal of this problem it to implement a binary min-heap using a linked-node binary tree. Each node stores a value and references to its left child, right child, and parent. The heap keeps the smallest value at the root and maintains a complete binary tree structure.

Algorithm: The program uses the position of each node in level order to find where new nodes belong. The binary representation of a position determines the path from the root, moving left for 0 and right for 1. When inserting a value, it is added to the next available position. If it is smaller than its parent, the values are swapped upward until the heap property is restored. When removing the minimum value, the last node replaces the root. The new root then moves downward as needed to restore the heap property. The implementation also includes methods for deleting values, building a heap, checking its size, and performing heap sort without changing the original heap. The heap is stored entirely using linked nodes instead of a list or array. The binary position method makes it possible to find the next available position in O(log n) time. 

How to run: I ran the commands below in the terminal from my HW6 folder. All the results matched the expected outputs in the assignment.

Commands:

Get-Content "Heap Resources/heap_input1.txt" | python problem2.py

Get-Content "Heap Resources/heap_input2.txt" | python problem2.py

Get-Content "Heap Resources/heap_input3.txt" | python problem2.py

Get-Content "Heap Resources/heap_input4.txt" | python problem2.py

Get-Content "Heap Resources/heap_input5.txt" | python problem2.py

Get-Content "Heap Resources/heap_input6.txt" | python problem2.py

Get-Content "Heap Resources/heap_input7.txt" | python problem2.py

Get-Content "Heap Resources/heap_input8.txt" | python problem2.py

Get-Content "Heap Resources/heap_input9.txt" | python problem2.py

Get-Content "Heap Resources/heap_input10.txt" | python problem2.py


Problem 3: The goal of this problem is to calculate the running median of a list of sales. After each new sale is added, the program calculates the median of all sales received so far. The program uses two heaps: a max-heap for the smaller half of the values and a min-heap for the larger half. 

Algorithm: The program inserts each new sale into the appropriate heap. It then checks the sizes of the heaps and moves values between them if needed to keep them balanced. The MaxHeap stores the smaller half of the values, with its largest value at the root. The MinHeap stores the larger half, with its smaller value at the root. If both heaps have the same number of values, the median is the average of their roots. If the MaxHeap has one extra value, its root is the median. This process repeats after every sale, and each median is added to the results list. Using two heaps means the program does not need to sort the sales after every insertion. The median can be found directly from the roots in O(1) time, while inserting and rebalancing values takes O(log n) time. The program also reuses the linked-nodes MinHeap implementation from Problem 2 and extends it to make a MaxHeap.

How to run: I ran the commands below in the terminal from my HW6 folder. All the results matched the expected outputs in the assignment.

Commands: 

Get-Content "Median Resources/median_input1.txt" | python problem3.py

Get-Content "Median Resources/median_input2.txt" | python problem3.py

Get-Content "Median Resources/median_input3.txt" | python problem3.py

Get-Content "Median Resources/median_input4.txt" | python problem3.py

Get-Content "Median Resources/median_input5.txt" | python problem3.py

Get-Content "Median Resources/median_input6.txt" | python problem3.py

Get-Content "Median Resources/median_input7.txt" | python problem3.py

Get-Content "Median Resources/median_input8.txt" | python problem3.py

Get-Content "Median Resources/median_input9.txt" | python problem3.py

Get-Content "Median Resources/median_input10.txt" | python problem3.py

Get-Content "Median Resources/median_input11.txt" | python problem3.py








