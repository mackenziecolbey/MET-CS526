# MET-CS526

Problem 1: sorting: For this problem, I implemented three different sorting algorithms: merge sort, quick sort, and insertion sort. Each program reads a list of integers from a text file and sorts the numbers in increasing order. I created three input files containing 15, 50, and 500 integers. The files include positive and negative numbers, and repeated values to make sure the algorithms can handle different types of inputs. None of the programs use Python's built-in sorting functions. Each sorting algorithm is implemented manually. 

1. Merge Sort

Merge sort uses a divide-and-conquer approach. Meaning that instead of sorting the whole list at once, the program breaks it into smaller parts, sorts those parts, and then puts them back together. First, the program checks if the list contains one or zero numbers. If it does, it is already sorted, if not, it finds the middle of the list and divides it into two halves. Then it calls Merge Sort again on each half, which keeps happening until the lists are small enough to be considered sorted. After that, the merge function combines the two sorted halves. It compares the first available number from each half and adds the smaller one to a new list. It continues doing that until all the numbers have been combined in the correct order. The rest of the numbers from either half are then added to the result. This produces the final sorted list. I used the Merge Sort because dividing the list into smaller sections makes it easier to sort larger amounts of data. It has a time complexity of O(n log n).

Running the program: I ran these commands in the python terminal:

python p1merge_sort.py Inputs/p1_small.txt

python p1merge_sort.py Inputs/p1_medium.txt

python p1merge_sort.py Inputs/p1_large.txt

Testing: I tested all three sorting algorithms using the same three input files containing 15, 50, and 500 integers. Each program prints the original values followed by the sorted values. I checked that the numbers were in increasing order and that negative numbers and repeated values were still included. All three algorithms successfully sorted all three input files. They also produced the same sorted results for each dataset.

2. Quick Sort

Quick sort also uses a divide-and-conquer approach, but it works differently from the Merge Sort. Instead of splitting the list into two equal halves, it uses a pivot to divide the numbers into smaller and larger groups. In my program, I chose the last number in the list as the pivot. The program compares every other number against that pivot. If a number is less than or equal to the pivot, it is added to the smaller list, if it's greater, it's added to the larger list. The program then calls Quick Sort again on both of the lists, then it continues dividing them until each list has zero or one number. Then, it combines the sorted smaller list, the pivot, and the sorted larger list. This puts the numbers in increasing order. I chose the last element as the pivot because it is simple to identify and use in the partitioning process. The pivot determines which group each number belongs to. Quick Sort usually has a time complexity of O(n log n), but it can take O(n^2) if the pivot repeatedly creates very uneven groups. 

Running the program: I ran these commands in the python terminal:

python p1quick_sort.py Inputs/p1_small.txt

python p1quick_sort.py Inputs/p1_medium.txt

python p1quick_sort.py Inputs/p1_large.txt

Testing: I tested all three sorting algorithms using the same three input files containing 15, 50, and 500 integers. Each program prints the original values followed by the sorted values. I checked that the numbers were in increasing order and that negative numbers and repeated values were still included. All three algorithms successfully sorted all three input files. They also produced the same sorted results for each dataset.

3. Insertion Sort

Insertion Sort works by building a sorted section of the list one number at a time. It is similar to organizing playing cards in your hand. The program starts at the second number because the first number is already considered sorted. It saves the current number and compares it with the numbers before it. If a previous number is larger, that number gets moved one position to the right. The program keeps doing this until it finds the correct position for the current number. It then inserts the number into that position. This process repeats until the program has gone through the entire list. I used this algorithm because it's a straightforward way to sort numbers and shows how a list can be sorted gradually without dividing it into smaller lists. However, it can take O(n^2) time because numbers may need to be shifted several positions. This can make it slower on larger lists compared to Merge Sort.

Running the program: I ran these commands in the python terminal:

python p1insertion_sort.py Inputs/p1_small.txt

python p1insertion_sort.py Inputs/p1_medium.txt

python p1insertion_sort.py Inputs/p1_large.txt

Testing: I tested all three sorting algorithms using the same three input files containing 15, 50, and 500 integers. Each program prints the original values followed by the sorted values. I checked that the numbers were in increasing order and that negative numbers and repeated values were still included. All three algorithms successfully sorted all three input files. They also produced the same sorted results for each dataset.


Problem 2:

For this problem, I implemented LSD (Least Significant) Radix Sort using base 10. The program sorts non-negative integers by looking at one digit at a time, starting with the ones digit and moving to the tens, hundreds, etc. I used Counting Sort for each digit pass. The program first reads the integers from the input file and stores them in a list. It then finds the largest number, so it knows how many digit passes are needed. The variable exp determines which digit it being sorted. It starts at 1 for the ones digit, then becomes 10 for the tens digit, 100 for the hundreds digit, and continues until all digits in the largest number have been processed. For each pass, the counting_sort function looks at the current digit of every number. It counts how many times each digit from 0 to 9 appears. Then, it adds the counts together to determine the position where the numbers should go in the output list. The function goes through the original list backwards when placing numbers in the output list. This keeps numbers with the same current digit in their original order, making the Counting Sort pass stable. Stability is important because Radix Sort processes the digits separately. When the next digit is sorted, the order established by the previous digit pass needs to be preserved for numbers with the same current digit. Without a stable sort, the earlier digit order can be lost, and the final numbers might not be sorted correctly. After each pass, the sorted list is used for the next digit. When the largest number has no more digits to process, the program prints the sorted list. The program also prints the original values before sorting so they can be compared with the sorted results. I used base 10, so each pass sorts based on one of the two possible digits (0 through 9). The program was tested with input files containing 15, 50, and 5000 non-negative integers. The files included repeated values and numbers with different numbers of digits. 

Running the program: I ran these commands in the python terminal:

python radix_sort.py inputs/p2_small.txt

python radix_sort.py inputs/p2_medium.txt

python radix_sort.py inputs/p2_large.txt


