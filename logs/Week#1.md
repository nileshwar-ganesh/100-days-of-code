### Day 0: Bubble Sort

Simple sorting algorithm, which compares adjacent elements and swaps values if needed.
This algorithm has **poor real world performance**, with a worst case complexity of O(n^2)

*Implementation*: my understanding of the algorithm is that after the first run, the largest number will be at the nth position. So for the next iteration can be reduced to n-1 runs, and then to n-2 runs and so on: as those slots will keep getting filled will numbers belonging in that position. also, during an iteration, no swap happens at all, that means the list is already in the right order.

*Learning*: instead of writing two different conditions for ascending and descending order, it is enough to multiply the numbers with 1 or -1 based on the required sort order. A single conditional statement for number comparison followed by the swap will then serve both purposes.

