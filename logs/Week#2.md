### Day 8: Tim Sort

This algorithm is derived from merge sort and insertion sort. It takes advantage of runs of consecutive ordered elements present in most real world data. The worst case complexity is O(n logn).

*Implementation*: the classical tim sort splits the given array into runs of size 32. However, dynamically setting the minimum run sizte based on input improves performance. Once we have the run size, split the array into runs and perform insertion sort on each run. And once sorted sub-arrays are in place, merge them back till only one run exists, which will be the sorted list.

*Learning*: shifting bitwise to the right halves the number (equivalent of n//2 in python). This can be used to effectively determine the run size.

### Day 9: Linear Search

A simple searching algorithm that sequentially checks each element in a list or array until a match is found or the entire list has been searched. The worst case complexity is O(n)

*Implementation*: the implementation is straight forward. Go through the list, starting from teh first element. If the element is found, return the index. If teh end of the list is reached and the element is not found, return -1 (not found)
