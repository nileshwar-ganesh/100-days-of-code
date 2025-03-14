def insertion_sort(numbers: list[int], reverse: bool = False) -> list[int]:
    """
    Sorts a list of numbers using insertion sort algorithm
    :param numbers: the input list of numbers in random order
    :param reverse: determines ascending or descending. ascending, by default.
    :return: the sorted list, as per the requirement
    """
    for index in range(1, len(numbers)):
        idx = index
        sign = -1 if reverse else 1
        while idx > 0 and sign * numbers[idx] < sign * numbers[idx - 1]:
            numbers[idx - 1], numbers[idx] = numbers[idx], numbers[idx - 1]
            idx -= 1
    return numbers

L = [32, 24, 10, 55, 89, 13, 23, 24]
print(insertion_sort(L))
print(insertion_sort(L, True))