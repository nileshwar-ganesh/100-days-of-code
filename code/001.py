def bubble_sort(numbers: list[int], reverse: bool = False) -> list[int]:
    """
    Sorts a list of numbers using bubble sort algorithm
    :param numbers: the input list of numbers in random order
    :param reverse: determines ascending or descending. ascending, by default.
    :return: the sorted list, as per the requirement
    """
    for iteration in range(len(numbers) - 1):
        is_swapped = False
        for index in range(len(numbers) - 1 - iteration):
            sign = -1 if reverse else 1
            if sign * numbers[index] > sign * numbers[index + 1]:
                numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
                is_swapped = True
        if not is_swapped:
            break
    return numbers

L = [32, 24, 10, 55, 89, 13, 23, 24]
print(bubble_sort(L))
print(bubble_sort(L, True))