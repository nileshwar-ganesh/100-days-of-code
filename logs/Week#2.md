### Day 8: Tim Sort

This algorithm is derived from merge sort and insertion sort. It takes advantage of runs of consecutive ordered elements present in most real world data. The worst case complexity is O(n logn).

*Implementation*: the classical tim sort splits the given array into runs of size 32. However, dynamically setting the minimum run sizte based on input improves performance. Once we have the run size, split the array into runs and perform insertion sort on each run. And once sorted sub-arrays are in place, merge them back till only one run exists, which will be the sorted list.

*Learning*: shifting bitwise to the right halves the number (equivalent of n//2 in python). This can be used to effectively determine the run size.
