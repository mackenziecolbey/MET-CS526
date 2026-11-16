# MET-CS526

Problem 1: This problem is to merge multiple sorted register logs into one sorted list of sales. Each register contains a list of sale times that is already sorted in increasing order. The program combines these lists and produces a final list of (time, register) pairs, where each pair represents a sale time and the register where the sale occurred. The merged list must be sorted by sale time. But, when two or more registers have sales at the same time, the sale from the register with the smaller register number must appear first. To do this, I made my own priority queue using a binary min-heap. 

Algorithm: The program uses a binary min-heap priority queue to efficiency keep track of the next sale that should be added to the merged list. The heart of the algorithm is that the priority queue only stores the next unprocessed sale from each nonempty register. Instead of asserting


The idea is to use the priority queue to keep track of the next sale from each register. Instead of putting every sale into
