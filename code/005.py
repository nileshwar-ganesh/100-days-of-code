def quick_sort(numbers: list[int], reverse=False) -> list[int]:
    """
    Sorts a list of numbers using quick sort algorithm
    :param numbers: the input list of numbers in random order
    :param reverse: determines ascending or descending. ascending, by default.
    :return: the sorted list, as per the requirement
    """
    sign = -1 if reverse else 1
    left = 0
    right = len(numbers) - 1
    sort_procedure(numbers, left, right, sign)
    return numbers

def sort_procedure(numbers: list[int], left: int, right: int, sign: int):
    """
    :param numbers: the list of numbers, that need to be sorted
    :param left: the left most index (of main and sub-lists, that keeps changing based on pivot index for higher side)
    :param right: the right most index (of main and sub-lists, that keeps changing based on pivot index for lower side)
    :param sign: determines the sort order, ascending or descending
    :return: returns nothing as it modifies the position directly in original list
    """
    if left < right:
        pivot = numbers[right]
        i = left
        for j in range(left, right):
            if sign * numbers[j] <= sign * pivot:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                i += 1
        numbers[i], numbers[right] = numbers[right], numbers[i]
        sort_procedure(numbers, left, i - 1, sign)
        sort_procedure(numbers, i + 1, right, sign)


L = [32, 24, 10, 55, 89, 13, 23, 24]
print(quick_sort(L))
print(quick_sort(L, True))
