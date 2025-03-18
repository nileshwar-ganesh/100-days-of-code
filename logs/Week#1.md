### Day 1: Bubble Sort

Simple sorting algorithm, which compares adjacent elements and swaps values if needed. This algorithm has poor real world performance, with a worst case complexity of O(n^2)

*Implementation*: my understanding of the algorithm is that after the first run, the largest number will be at the nth position. So for the next iteration can be reduced to n-1 runs, and then to n-2 runs and so on: as those slots will keep getting filled will numbers belonging in that position. also, during an iteration, no swap happens at all, that means the list is already in the right order.

*Learning*: instead of writing two different conditions for ascending and descending order, it is enough to multiply the numbers with 1 or -1 based on the required sort order. A single conditional statement for number comparison followed by the swap will then serve both purposes.

### Day 2: Selection Sort

Another simple sorting algorithm, which looks for lowest value inside the list per iteration and moves it to the front. Performs poorly with large data, with a worst case complexity of O(n^2)

*Implementation*: my understanding of the algorithm is that in every iteration, we look for the smallest number in the unsorted portion of the list and move it up to the front. So in the first step, the number at position 1 gets swapped with the lowest value which follows. In the next step, the number at position 2 gets swapped with the next lowest value and so on.

### Day 3: Insertion Sort

This simple sorting agorithm divides the input into sorted and unsorted region, inserting an element from unsorted region into the sorted one, one at a time. The worst case complexity is O(n^2)

*Implementation*: my understanding is to consider an element from unsorted region, compare it with elements in the sorted region and swap places if the condition is met. As soon as the condition becomes false, it means that the element has reached its position for now. So stop and move on to the next element in unsorted region.

### Day 4: Merge Sort

It is a general purpose, comparison sorting algorithm, which uses divide and conquer method. It has a time complexity of O(n logn)

*Implementation*: my understanding is that the algorithm has two parts. The first one repetedly keeps dividing the array into halves, till only single element arrays remain. Then repeatedly merge elements into sorted sublists, till all elements form a single sorted array.

*Learning*: using recursion helps in tackling this problem easily. The function finds the mid point and calls the same function twice, with [left, mid] and [mid+1, right] as the next input. Then it compares the elements in the sublists starting from left, and modify the original array in its right position.

### Day 5: Quick Sort

It is an efficient, general purpose algorithm which is slightly faster than merge sort and heap sort. The algorithm employs divide and conquer method, and has average complexity of O(n logn) and worst case complexity of O(n^2)

*Implementation*: my understanding is that the procedure revolves around something called as a pivot element. This element is randomly chosen. The numbers less than pivot element are arranged on the left side and the others on the right side (ascending sort) with pivot element in the middle. Then both left and right arrays (excluding the pivot element) are fed recursively into the sorting algorithm. Whenever left limit value becomes greater or equal to right limit value (in case of single element left in sub-arrays), the algorithm stops.

### Day 6: Heap Sort

This is a comparison based sorting algorithm, which uses a binary heap data structure to sort elements in an array. The worst case complexity is O(n logn).

*Implementation*: my understanding is that the algorithm runs in two phases.

In the first phase, we build a max heap from given random array. Now the question arises, "What is a valid Max Heap?" In a valid max heap, the value of each parent node is greater than or equal to the value of its children. That means the root element is always the largest element in the heap.

In the second phase, we do the actual sorting. We already know that the max heap from phase 1 has the largest element on the top. We move it to the last position in the array. Now, we have to re-heap the (1, .., n-1) elements, so that the next largest element is at the top of the heap. So we call heapify function again. And this will go on from indices n to 1, till teh entire list is sorted.

*Learning*: in order to create a binary tree from an array, for any index *i*, the child nodes will always be *2 x i + 1* and *2 x i + 2*

### Day 7: Radix Sort

A non-comparative sorting algorithm that sorts data by grouping keys based on individual digits, which share the same significant position. This algorithm requires extra space for sorting, as it is not in-place sorting algorithm. The time complexity is O(n logM), where M is the maximum value present in the list.

*Implementation*: my understanding is that this algorithm employs modified version of another algorithm (counting sort) as a sub-routine. Counting sort sub-routine basically follows following step: keep track of count of digits (0-9) appearing in the same significant position, create a cumulative sum (from front or rear, based on sort order) and then sort the numbers based on cumulative sum. The algorithm runs this routine for d iterations, where d is number of digits present in the number with maximum value.

*Learning*: radix sort does not handle negative numbers. A workaround is to separate negative and positive numbers initially and then run the radix sort separately on both lists. And then, combine both results at the end to get the final result.
