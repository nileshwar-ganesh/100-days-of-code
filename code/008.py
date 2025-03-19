import random

def tim_sort(numbers: list[int], reverse: bool = False):
    """
    :param numbers: list of numbers to be sorted
    :param reverse: ascending or descending order
    :return: the sorted array
    :explanation:
        The classical Timsort algorithm has the following steps:
            1. split the array into runs of 32
            2. sort each run using insertion sort
            3. merge sorted runs back in order
        Repeat this process till only one single run remains
    """
    # this takes care of empty array
    if not numbers:
        return numbers

    # determine the length of the run
    total_length = len(numbers)
    additional_bit = 0
    while total_length >= 64:
        additional_bit |= total_length & 1
        total_length >>= 1
    run_size = total_length + additional_bit

    # create runs based on the previously determined size
    runs = []
    for i in range(0, len(numbers), run_size):
        run = numbers[i:min(i+run_size, len(numbers))]
        # apply insertion sort on individual runs, before collecting them
        runs.append(insertion_sort(run, reverse))

    # merge the sorted runs
    while len(runs) > 1:
        new_runs = []
        # merge two adjacent runs
        for i in range(0, len(runs) - 1, 2):
            new_runs.append(merge_procedure(runs[i], runs[i+1], reverse))
        # in case of odd number of runs, simply add the last one, as there is no option to merge for now
        if len(runs) % 2 == 1:
            new_runs.append(runs[-1])
        runs = new_runs
    return runs

def insertion_sort(numbers: list[int], reverse: bool) -> list[int]:
    numbers = numbers[:]
    for index in range(1, len(numbers)):
        idx = index
        sign = -1 if reverse else 1
        while idx > 0 and sign * numbers[idx] < sign * numbers[idx - 1]:
            numbers[idx - 1], numbers[idx] = numbers[idx], numbers[idx - 1]
            idx -= 1
    return numbers

def merge_procedure(array_1, array_2, reverse: bool):
    sign = -1 if reverse else 1
    # starting both left and right sides from starting position
    i = j = k = 0
    sorted_array = [None] * (len(array_1) + len(array_2))
    # merge with O(n) time
    while i < len(array_1) and j < len(array_2):
        if sign * array_1[i] <= sign * array_2[j]:
            sorted_array[k] = array_1[i]
            i += 1
        else:
            sorted_array[k] = array_2[j]
            j += 1
        k += 1
    # if elements still remain
    while i < len(array_1):
        sorted_array[k] = array_1[i]
        i += 1
        k += 1
    while j < len(array_2):
        sorted_array[k] = array_2[j]
        j += 1
        k += 1
    return sorted_array

large_array = [random.randint(-64, 64) for _ in range(64)]
print(large_array)
print(tim_sort(large_array))
print(tim_sort(large_array, True))
