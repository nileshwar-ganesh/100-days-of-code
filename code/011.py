import math

def jump_search(array, key):
    jump_length = math.floor(math.sqrt(len(array)))
    for i in range(0, len(array), jump_length):
        if key > array[min(i + jump_length, len(array)) - 1]:
            continue
        for j in range(i, min(i + jump_length, len(array))):
            if array[j] == key:
                return "The item exists."

    return "The item does not exist."


"""
Using Heap Sort to sort the given list before binary search
For detailed explanation on how heap sort works, check Day 006 implementation
"""
def heapify(numbers: list[int], total_count: int, root_index: int, sign: int):
    index_largest_value = root_index
    index_left_child = 2 * root_index + 1
    index_right_child = 2 * root_index + 2
    if index_left_child < total_count and sign * numbers[index_left_child] > sign * numbers[index_largest_value]:
        index_largest_value = index_left_child
    if index_right_child < total_count and sign * numbers[index_right_child] > sign * numbers[index_largest_value]:
        index_largest_value = index_right_child
    if index_largest_value != root_index:
        numbers[index_largest_value], numbers[root_index] = numbers[root_index], numbers[index_largest_value]
        heapify(numbers, total_count , index_largest_value, sign)

def heap_sort(numbers: list[int], reverse: bool=False) -> list[int]:
    sign = -1 if reverse else 1
    total_count = len(numbers)
    for root_index in range(total_count // 2 - 1, -1, -1):
        heapify(numbers, total_count, root_index, sign)
    for index in range(total_count - 1, -1, -1):
        numbers[index], numbers[0] = numbers[0], numbers[index]
        heapify(numbers, index, 0, sign)
    return numbers


L = [32, 24, 10, 55, 89, 13, 23, 24]
L = heap_sort(L)
print(jump_search(L, 89))

