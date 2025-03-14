### Day 0: Bubble Sort

Simple sorting algorithm, which compares adjacent elements and swaps values if needed. This algorithm has poor real world performance, with a worst case complexity of O(n^2)

*Implementation*: my understanding of the algorithm is that after the first run, the largest number will be at the nth position. So for the next iteration can be reduced to n-1 runs, and then to n-2 runs and so on: as those slots will keep getting filled will numbers belonging in that position. also, during an iteration, no swap happens at all, that means the list is already in the right order.

*Learning*: instead of writing two different conditions for ascending and descending order, it is enough to multiply the numbers with 1 or -1 based on the required sort order. A single conditional statement for number comparison followed by the swap will then serve both purposes.

### Day 1: Selection Sort

Another simple sorting algorithm, which looks for lowest value inside the list per iteration and moves it to the front. Performs poorly with large data, with a worst case complexity of O(n^2)

*Implementation*: my understanding of the algorithm is that in every iteration, we look for the smallest number in the unsorted portion of the list and move it up to the front. So in the first step, the number at position 1 gets swapped with the lowest value which follows. In the next step, the number at position 2 gets swapped with the next lowest value and so on.

### Day 2: Insertion Sort

This simple sorting agorithm divides the input into sorted and unsorted region, inserting an element from unsorted region into the sorted one, one at a time. The worst case complexity is O(n^2)

*Implementation*: my understanding is to consider an element from unsorted region, compare it with elements in the sorted region and swap places if the condition is met. As soon as the condition becomes false, it means that the element has reached its position for now. So stop and move on to the next element in unsorted region.

