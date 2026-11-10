# MET-CS526

Problem 1: this creates a Binary Tree Search using 2 classes: Node and BST. Each node stores a number and has a left and right child. The program generates a random set of 5 to 50 numbers between 1 and 1000 and uses them to build the tree. Then, it tests the different methods needed for this problem. 

Algorithm: The node class stores a value and its left and right children. When a node is created, both children are initially empty (none). AddNode(Value) adds a new number to the tree. Smaller numbers go to the left, then larger numbers go to the right. This will continue until an empty spot is found. The DeleteNode(Value) finds and removes a number from the tree. if the node has 2 children, it replaces the value with the smallest number in its right subtree to keep the tree in order. The FindNode(Value) searches the tree for a number. It moves left or right depending on whether the number is smaller or larger than the current node. It returns True if the number is found and False if it is not. PrintTree() prints the tree using in-order traversal. It visits the left child, the current node, and then the right child, which prints the numbers in ascending order.
The program generates and prints a set of numbers, builds the initial binary tree and prints it, then adds a new number and prints the updated tree. The program then searches for a number that exists in the tree, then searches for a number that does not exist in the tree.

How to run: I ran the binary_search_tree.py in PyCharm, and the results appeared in the Run window. The program successfully ran and created a binary tree and demonstrates adding, deleting, searching, and printing nodes. The tree also stays in the correct order after each operation.


Problem 2: This program calculates how many different combinations of vowels can be created from a sequence of dots and dashes in Morse code. It uses the Morse code representations of A, E, I, O, and U. The program reads an input file provided through the terminal. The first line contains the length of the sequence, and the second line contains the Morse code.

Algorithm: The program uses Dynamic Programming to count the possible vowel combinations. It starts by creating a list called dp, which stores the number of possible combinations up to each position in the sequence. It starts with dp[0]=1, which represents one way to form an empty sequence. The program checks each position to see if it ends with the Morse code for one of the 5 vowels. If a match is found, than it adds the number of combinations from the previous position to the current count. When the entire sequence has been checked, the last value in the dp list gives the total number of possible vowel combinations.

How to run: I ran the commands below in the terminal from my HW5 folder. All results matches the expected outputs in the assignment.

Commands:

python vowel_combination.py vowel_input1.txt

python vowel_combination.py vowel_input2.txt

python vowel_combination.py vowel_input3.txt

python vowel_combination.py vowel_input4.txt

Results: the results were as follows

vowel_input1.txt: 6 combinations

vowel_input2.txt: 8 combinations

vowel_input3.txt: 0 combinations

vowel_input4.txt: 193050000 combinations


Problem 3


 



