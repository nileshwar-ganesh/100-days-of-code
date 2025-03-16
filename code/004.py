def merge_sort(numbers: list[int], reverse=False) -> list[int]:
    """
    Sorts a list of numbers using merge sort algorithm
    :param numbers: the input list of numbers in random order
    :param reverse: determines ascending or descending. ascending, by default.
    :return: the sorted list, as per the requirement
    """
    left = 0
    right = len(numbers) - 1
    sign = -1 if reverse else 1
    sort_procedure(numbers, left, right, sign)
    return numbers

def sort_procedure(numbers: list[int], left: int, right: int, sign: int):
    """
    :param numbers: the list of numbers, that need to be sorted
    :param left: the left most index (of main and sub-lists, that keeps changing based on mid-point)
    :param right: the right most index (of main and sub-lists, that keeps changing based on mid-point)
    :param sign: determines the sort order, ascending or descending
    :return: returns nothing as it modifies the position directly in original list
    """
    if left < right:
        mid = (left + right) // 2
        # splitting into groups
        sort_procedure(numbers, left, mid, sign)
        sort_procedure(numbers, mid + 1, right, sign)
        # merging back based on order
        left_array = numbers[left:mid + 1]
        right_array = numbers[mid + 1: right + 1]

        # starting both left and right sides from starting position
        i = j = 0
        # the position in the original array
        k = left
        # merge with O(n) time
        while i < len(left_array) and j < len(right_array):
            if sign * left_array[i] <= sign * right_array[j]:
                numbers[k] = left_array[i]
                i += 1
            else:
                numbers[k] = right_array[j]
                j += 1
            k += 1
        # if elements still remain
        while i < len(left_array):
            numbers[k] = left_array[i]
            i += 1
            k += 1
        while j < len(right_array):
            numbers[k] = right_array[j]
            j += 1
            k += 1

L = [32, 24, 10, 55, 89, 13, 23, 24]
print(merge_sort(L))
print(merge_sort(L, True))
