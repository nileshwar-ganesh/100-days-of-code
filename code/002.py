def selection_sort(numbers: list[int], reverse: bool = False) -> list[int]:
    """
    Sorts a list of numbers using selection sort algorithm
    :param numbers: the input list of numbers in random order
    :param reverse: determines ascending or descending. ascending, by default.
    :return: the sorted list, as per the requirement
    """
    for index in range(len(numbers) - 1):
        min_value, min_index = numbers[index], index
        for idx in range(index + 1, len(numbers)):
            sign = -1 if reverse else 1
            if sign * numbers[idx] < sign * min_value:
                min_value, min_index = numbers[idx], idx
        numbers[index], numbers[min_index] = numbers[min_index], numbers[index]
    return numbers

L = [32, 24, 10, 55, 89, 13, 23, 24]
print(selection_sort(L))
print(selection_sort(L, True))