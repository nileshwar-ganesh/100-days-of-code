### Day 8: Tim Sort

This algorithm is derived from merge sort and insertion sort. It takes advantage of runs of consecutive ordered elements present in most real world data. The worst case complexity is O(n logn).

*Implementation*: the classical tim sort splits the given array into runs of size 32. However, dynamically setting the minimum run sizte based on input improves performance. Once we have the run size, split the array into runs and perform insertion sort on each run. And once sorted sub-arrays are in place, merge them back till only one run exists, which will be the sorted list.

*Learning*: shifting bitwise to the right halves the number (equivalent of n//2 in python). This can be used to effectively determine the run size.

### Day 9: Linear Search

A simple searching algorithm that sequentially checks each element in a list or array until a match is found or the entire list has been searched. The worst case complexity is O(n)

*Implementation*: the implementation is straight forward. Go through the list, starting from teh first element. If the element is found, return the index. If teh end of the list is reached and the element is not found, return -1 (not found)

### Day 10: Binary Search

An effiient searching algorithm, which works by repeatedly dividing the search range in half. It can only be used on sorted arrays. The complexity of search is O(logn). When coupled with a sorting algorithm, the complexity becomes O(n logn).

*Implementation*: it follows these steps - find middle element, and if they match return the found status/index. If target is smaller, search left half. Else, search right half. Repeat until element is found or the range is exhausted.

### Day 11: Jump Search

An efficient searching algorithm designed for sorted arrays. It strikes a balance between linear search and binary search. The worst case complexity is O(sqrt(n)).

*Implementation*: the jump length is given by square root of total number of elements. In every iteration we take elements in batches of sqrt(n) elements. If the last element is less than the key value, we jump to next batch of sqrt(n) elements. Once we find the right batch, we conduct a linear search within it, to check for the element.

### Day 12: Median of Two Sorted Arrays problem

*Problem Statement*: Given two sorted arrays of sizes m and n, find the median of the combined sorted array without fully merging them. Time complexity is O(log(min(m, n))).

*Implementation*: perform binary search on smaller array. Partition both arrays, such that left half contains smaller elements and then compute the median.
