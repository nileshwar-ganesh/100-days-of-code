def find_median(array_1, array_2):
    """
    :param array_1: list of numbers
    :param array_2: other list of numbers
    :return:
    :explanation:
        The objective is to find the median of two sorted arrays without actually merging them.

        Instead of merging the arrays, we use binary search on the smaller array to find a partition where the left
        half contains the smaller elements and the right half contains the larger elements.

        Example 1:
        array_1 = [1, 5, 9]
        array_2 = [2, 3, 7, 8]
        Merged (for understanding): [1, 2, 3, 5, 7, 8, 9]
        Since the total number of elements is odd (7), the median is the middle element → 5

        Example 2:
        array_1 = [1, 5, 9]
        array_2 = [2, 3, 7]
        Merged (for understanding): [1, 2, 3, 5, 7, 9]
        Since the total number of elements is even (6), the median is the average of the two middle elements:
        (3 + 5) / 2 = 4.0

        Key Idea:
        Instead of merging the arrays (O(m+n) time), we use binary search (O(log min(m, n))) to efficiently find
        the correct partition and compute the median.

        Edge Cases:
        - One array is empty → return the median of the other array.
        - Arrays of different lengths.
    """

    if not array_1 and not array_2:
        return "Both arrays are blank."

    if not array_1:
        mid = len(array_2) // 2
        if len(array_2) % 2 == 0:
            return "The median is " + str((array_2[mid] + array_2[mid-1])/2)
        else:
            return "The median is " + str(array_2[mid])

    if not array_2:
        mid = len(array_1) // 2
        if len(array_1) % 2 == 0:
            return "The median is " + str((array_1[mid] + array_1[mid-1])/2)
        else:
            return "The median is " + str(array_1[mid])

    if len(array_1) <= len(array_2):
        i, j = binary_search(array_1, array_2, 0, len(array_1))
    else:
        j, i = binary_search(array_2, array_1, 0, len(array_2))

    max_left = max(array_1[i - 1] if i > 0 else float('-inf'),
                   array_2[j - 1] if j > 0 else float('-inf'))

    min_right = min(array_1[i] if i < len(array_1) else float('inf'),
                    array_2[j] if j < len(array_2) else float('inf'))

    if (len(array_1) + len(array_2)) % 2 == 0:
        return "The median is " + str((max_left + min_right) / 2)
    else:
        return "The median is " + str(max_left)


def binary_search(array_small, array_large, left, right):
    if left <= right:
        i = (left + right) // 2
        j = ((len(array_small) + len(array_large) + 1) // 2) - i
        small_i_m = array_small[i - 1] if i > 0 else float('-inf')
        small_i = array_small[i] if i >= 0 else float('inf')
        large_j_m = array_large[j - 1] if j > 0 else float('-inf')
        large_j = array_large[j] if j >= 0 else float('inf')
        if small_i_m <= large_j and large_j_m <= small_i:
            return i, j
        if small_i_m > large_j:
            return binary_search(array_small, array_large, left, i - 1)
        elif large_j_m > small_i:
            return binary_search(array_small, array_large, i + 1, right)

# Test Case
A = [1, 3, 8, 9, 15]
B = [7, 11, 18, 19, 21, 25]

print(find_median(A, B))
