def radix_sort(numbers: list[int], reverse: bool = False) -> list[int]:
    """
    :param numbers: list of numbers to be sorted
    :param reverse: determines ascending or descending. ascending, by default.
    :return: returns the sorted array

    :explanation:
        to include negative numbers, first separate numbers based on sign
        then run the conventional radix sort separately on both arrays
        and finally merge them together

        the sort order for negative numbers will always be the opposite of reverse variable
        while returning the sorted values, the negative numbers will be appended to front end for ascending order
        for descending order, the negative numbers will be appended to the rear end
    """
    negative_numbers = [-num for num in numbers if num < 0]
    positive_numbers = [num for num in numbers if num >= 0]
    negative_sort = _radix_sort(negative_numbers, not reverse)
    positive_sort = _radix_sort(positive_numbers, reverse)
    if reverse:
        return positive_sort + [-num for num in negative_sort]
    else:
        return [-num for num in negative_sort] + positive_sort


def _radix_sort(numbers: list[int], reverse: bool = False) -> list[int]:
    """
    :param numbers: list of numbers to be sorted
    :param reverse: determines ascending or descending. ascending, by default.
    :return: returns the sorted array

    :explanation:
        total time complexity = O(d.(n+k))
        since k is constant, it does not contribute to asymptotic growth
        final time complexity = O(n logM)

        but this implementation of radix sort does not handle negative numbers, as it is digit based comparison.
    """
    if not numbers:
        return numbers
    denominator = 1
    # iterations d = log M + 1 (number of digits in maximum number)
    for _ in range(len(str(max(numbers)))):
        numbers = counting_sort(numbers, denominator, reverse)
        denominator *= 10
    return numbers


def counting_sort(numbers: list[int], denominator: int, reverse: bool = False):
    """
    :param numbers: list of numbers to be sorted
    :param denominator: useful for digit wise comparison starting from least significant to most (1, 10, 100, ...)
    :param reverse: determines the sort order
    :return:

    :explanation:
        counting sort is a standalone sorting algorithm on its own. a modified version of it is used as a subroutine.
    """
    total_length = len(numbers)
    sorted_array = [0] * total_length
    count_values = [0] * 10

    # counting digit occurrence O(n)
    for num in numbers:
        digit = (num // denominator) % 10
        count_values[digit] += 1

    # cumulative sum O(k), where k=10 (0, .., 9)
    if reverse:
        for i in range(len(count_values) - 2, -1, -1):
            count_values[i] += count_values[i + 1]
    else:
        for i in range(1, len(count_values)):
            count_values[i] += count_values[i-1]

    # sorting based on cumulative sum, O(n)
    for i in range(len(numbers) - 1, -1, -1):
        digit = (numbers[i] // denominator) % 10
        sorted_array[count_values[digit] - 1] = numbers[i]
        count_values[digit] -= 1

    # total time complexity O(n + k)
    return sorted_array

L = [32, 24, 10, 55, -89, 13, 23, 24, -55]
print(radix_sort(L))
print(radix_sort(L, True))